import google.api_core.exceptions
import google.auth.credentials
import google.cloud.pubsub
import googleapiclient.discovery
import googleapiclient.errors
import random
import re
import string
import time
import typing


class GCEConfig(typing.NamedTuple):
    """
    A simple data class to store configuration information for the Google Compute Engine.

    project_id: The GCE project name in which to create everything.
    zone: The zone in which to create everything
    credentials: The credentials to use locally to create everything. Must have permissions to delete and create:
        * PubSub topics
        * PubSub subscriptions
        * Instance templates
        * Managed instance groups
    service_account: The service account to use on the created GCE VMs. Must have permissions to:
        * Read from PubSub subscriptions
        * Read/Write to google cloud storage
        * Delete instance from managed instance group
        * Delete instance
    """

    project_id: str
    zone: str
    credentials: google.auth.credentials.Credentials
    service_account: str


class GCEEngine:
    """
    An engine to run shell scripts on a docker image in the google cloud.

    This class is immutable; all engine state is obtained from GCE as needed.
    """

    def __init__(self, engine_id: str, image: str, config: GCEConfig):
        """
        Create a engine to run shell scripts on a docker image in the google cloud.

        :param engine_id: A unique identifier for this engine, used as the resource id for the associated topic,
                          subscription, and instance template.
        :param image: The GCE identifier of a docker image to run.
        :param config: GCE configuration information
        """
        self._id = engine_id
        self._image = image
        self._config = config

        self._publisher = google.cloud.pubsub.PublisherClient(
            **{"credentials": self._config.credentials}
        )
        self._topic_path = self._publisher.topic_path(self._config.project_id, self._id)

        self._subscriber = google.cloud.pubsub.SubscriberClient(
            **{"credentials": self._config.credentials}
        )
        self._subscription_path = self._subscriber.subscription_path(
            self._config.project_id, self._id
        )

        self._compute = googleapiclient.discovery.build(
            "compute", "v1", credentials=self._config.credentials
        )

        self._prepare_queue()

    def _prepare_queue(self):
        """
        Prepare the queue to add tasks to this engine.

        :return: None
        """
        try:
            self._publisher.create_topic(self._topic_path)
            print("Created topic " + self._topic_path)
        except google.api_core.exceptions.AlreadyExists:
            pass

        try:
            self._subscriber.create_subscription(
                self._subscription_path, self._topic_path, ack_deadline_seconds=60
            )
            print("Created subscription " + self._subscription_path)
        except google.api_core.exceptions.AlreadyExists:
            pass

    def add_task(
        self,
        script: str,
        inputs: typing.List[typing.Tuple[str, str]] = None,
        outputs: typing.List[typing.Tuple[str, str]] = None,
    ):
        """
        Assign an additional task to this engine. A task consists of a script, together with some specified inputs.

        The script will ultimately be run on the provided image with a working directory containing only the script.
        [inputs] is a list of files to copy into the working directory from GCS before running the script.
        [outputs] is a list of files or directories to copy from the working directory to GCS after running the script.

        Note that this method can only be run after .prepare_queue() has been called.

        :param script: The script to run as part of this task.
        :param inputs: Files to copy from GCS, as a list of ([local path], [GCS blob id]) pairs.
        :param outputs: Files or directories to copy to GCS, as a list of ([local path], [GCS blob id]) pairs.
        :return:
        """
        if inputs is None:
            inputs = []
        if outputs is None:
            outputs = []

        attributes = {}
        for local, remote in inputs:
            attributes["SOURCE " + local] = remote
        for local, remote in outputs:
            attributes["UPLOAD " + local] = remote

        try:
            self._publisher.publish(
                self._topic_path, bytes(script, "UTF-8"), **attributes
            )
        except google.api_core.exceptions.NotFound:
            # Create the topic and retry
            self._prepare_queue()
            self._publisher.publish(
                self._topic_path, bytes(script, "UTF-8"), **attributes
            )

    def _prepare_template(
        self,
        template_id: str,
        machine_type: str,
        preemptible: bool,
        accelerators: typing.List[typing.Tuple[str, int]],
        delete_when_done: bool,
    ):
        """
        Construct an instance template for a VM that can process tasks given to this engine.
        Delete the previous instance template by this name if any exists.

        There is no public API for constructing a container spec (without going through GKE
        or the online console), so this may be fragile.

        :param template_id: The id to use for the created template.
        :param machine_type: The machine type to use for the specification.
        :param preemptible: True if the VM should be preemptible, otherwise false.
        :param accelerators: A list of (name, count) for each accelerator to be included.
        :param delete_when_done: True if the VM should delete itself when no tasks exist.
        :return: None
        """

        # Delete this template if it already exists
        delete_if_exists(
            self._compute.instanceTemplates(),
            wait=True,
            project=self._config.project_id,
            instanceTemplate=template_id,
        )

        # Environment variables to include when running the docker image
        environment_vars = {"GCE_SUBSCRIPTION": self._subscription_path}
        if not delete_when_done:
            environment_vars[
                "RETRY_DELAY"
            ] = 15  # instead of deleting the worker, recheck the queue every 15s.

        # Prepare the container spec
        # This container declaration format is not public API and may change without notice.
        # ... so if something breaks, look here first.
        environment_spec = ["      env:"]
        for name, value in environment_vars.items():
            environment_spec += [
                "        - name: " + str(name),
                "          value: " + str(value),
            ]
        container_spec = "\n".join(
            [
                "spec:",
                "  containers:",
                "    - name: {container_name}".format(container_name=self._id),
                "      image: '{container_image}'".format(container_image=self._image),
                "      command:",
                "        - python",
                "      args:",
                "        - '-c'",
                "        - import turbine; turbine.run()",
            ]
            + environment_spec
            + ["      stdin: false", "      tty: false", "  restartPolicy: Never\n\n"]
        )

        # This value also probably needs to be updated occasionally
        parent_vm_image = "cos-stable-78-12499-89-0"

        template = {
            "name": template_id,
            "description": "",
            "properties": {
                "machineType": machine_type,
                "displayDevice": {"enableDisplay": False},
                "metadata": {
                    "kind": "compute#metadata",
                    "items": [
                        {"key": "gce-container-declaration", "value": container_spec},
                        {"key": "google-logging-enabled", "value": "true"},
                    ],
                },
                "tags": {"items": []},
                "disks": [
                    {
                        "kind": "compute#attachedDisk",
                        "type": "PERSISTENT",
                        "boot": True,
                        "mode": "READ_WRITE",
                        "autoDelete": True,
                        "deviceName": self._id,
                        "initializeParams": {
                            "sourceImage": "projects/cos-cloud/global/images/{vm_image}".format(
                                vm_image=parent_vm_image
                            ),
                            "diskType": "pd-standard",
                            "diskSizeGb": "10",
                            "labels": {},
                        },
                    }
                ],
                "canIpForward": False,
                "networkInterfaces": [
                    {
                        "kind": "compute#networkInterface",
                        "network": "projects/{project_id}/global/networks/default".format(
                            project_id=self._config.project_id
                        ),
                        "accessConfigs": [
                            {
                                "kind": "compute#accessConfig",
                                "name": "External NAT",
                                "type": "ONE_TO_ONE_NAT",
                                "networkTier": "PREMIUM",
                            }
                        ],
                        "aliasIpRanges": [],
                    }
                ],
                "labels": {"container-vm": parent_vm_image},
                "scheduling": {
                    "preemptible": preemptible,
                    "onHostMaintenance": "TERMINATE",
                    "automaticRestart": False,
                    "nodeAffinities": [],
                },
                "reservationAffinity": {"consumeReservationType": "ANY_RESERVATION"},
                "serviceAccounts": [
                    {
                        "email": self._config.service_account,
                        "scopes": ["https://www.googleapis.com/auth/cloud-platform"],
                    }
                ],
            },
        }

        # Add any hardware accelerators
        if accelerators is not None:
            template["properties"]["guestAccelerators"] = [
                {"acceleratorType": accelerator[0], "acceleratorCount": accelerator[1]}
                for accelerator in accelerators
            ]

        # Create the template
        GCEOperation(
            self._compute,
            self._compute.instanceTemplates()
            .insert(project=self._config.project_id, body=template)
            .execute(),
        ).wait()

    def start(
        self,
        target_size: int,
        worker_id: str = None,
        machine_type: str = "n1-standard-1",
        preemptible: bool = True,
        accelerators: typing.List[typing.Tuple[str, int]] = None,
        delete_when_done: bool = True,
    ):
        """
        Start an instance group to process tasks given to this engine. All VMs in the instance group will automatically
        delete themselves when the engine has no tasks left, unless delete_when_done is set.

        :param target_size: The number of VMs (<=500) to target in the instance group.
        :param worker_id: An additional, optional identifier for this worker. Will be randomized if not set.
        :param machine_type: The machine type to use for the specification.
        :param preemptible: True if the VM should be preemptible, otherwise false.
        :param accelerators: A list of (name, count) for each accelerator to be included.
        :param delete_when_done: True if the VM should delete itself when no tasks exist.
        :return: None
        """

        if target_size > 500:
            raise RuntimeError(
                "Maximum allowed target size of 500"
            )  # Otherwise I have to figure out REST pagination

        if worker_id is None:
            worker_id = "".join(random.choice(string.ascii_lowercase) for _ in range(4))

        template_id = self._id + "-" + worker_id
        self._prepare_template(
            template_id, machine_type, preemptible, accelerators, delete_when_done
        )

        GCEOperation(
            self._compute,
            self._compute.instanceGroupManagers()
            .insert(
                project=self._config.project_id,
                zone=self._config.zone,
                body={
                    "name": template_id,
                    "instanceTemplate": "projects/{project_id}/global/instanceTemplates/{id}".format(
                        project_id=self._config.project_id, id=template_id
                    ),
                    "baseInstanceName": template_id,
                    "targetSize": target_size,
                },
            )
            .execute(),
        ).wait()
        print("Started managed instance group " + template_id)

    def workers(self):
        """
        Find all workers currently running tasks for this engine.
        :return:
        """

        def delete_instance_group_manager(name):
            """
            Delete the provided instance group manager in this project. Block until deleted.

            :param name: The name of the instance group manager to delete.
            :return: None
            """
            print("Deleting instance group manager " + name)
            delete_if_exists(
                self._compute.instanceGroupManagers(),
                wait=True,
                project=self._config.project_id,
                zone=self._config.zone,
                instanceGroupManager=name,
            )

        def delete_instance_template(name):
            """
            Delete the provided instance template in this project. Block until deleted.

            :param name: The name of the instance group manager to delete.
            :return: None
            """
            print("Deleting instance template " + name)
            delete_if_exists(
                self._compute.instanceTemplates(),
                wait=True,
                project=self._config.project_id,
                instanceTemplate=name,
            )

        class InstanceGroupWorker:
            def __init__(self, base):
                self._base = base

            def __getitem__(self, name):
                return self._base[name]

            def stop(self, force_stop=True):
                """
                Delete the instance group and associated template. Block until deleted.

                :param force_stop: If False, an exception will be raised if the group still has active workers.
                :return: None
                """
                if self["targetSize"] > 0 and not force_stop:
                    raise Exception(
                        "Instance group {name} has {num} workers running".format(
                            name=self["name"], num=self["targetSize"]
                        )
                    )
                delete_instance_group_manager(self["name"])
                delete_instance_template(self["name"])

            @property
            def info(self):
                return self._base

            def __str__(self):
                return "$worker[{name}, {size}]".format(
                    name=self["name"], size=self["targetSize"]
                )

        # Find all instance groups that were created with this engine's instance template
        instance_groups = (
            self._compute.instanceGroupManagers()
            .list(project=self._config.project_id, zone=self._config.zone)
            .execute()
        )
        result = []
        if "items" in instance_groups:
            for group in instance_groups["items"]:
                if (
                    group["instanceTemplate"].find("instanceTemplates/" + self._id)
                    != -1
                ):
                    result.append(InstanceGroupWorker(group))
        return result

    def stop(self, force_stop=True):
        """
        Delete all workers provisioned by this engine. Block until deleted.

        :param force_stop: If False, an exception will be raised if the group still has active workers.
        :return: None
        """
        for worker in self.workers():
            worker.stop(force_stop=force_stop)

    def cleanup(self, force_stop=True):
        """
        Delete all resources provisioned by this engine. Block until deleted.

        :param force_stop: If False, an exception will be raised if the group still has active workers.
        :return: None
        """
        for worker in self.workers():
            worker.stop(force_stop=force_stop)

        try:
            self._subscriber.delete_subscription(self._subscription_path)
            print("Deleted subscription " + self._subscription_path)
        except:
            pass
        try:
            self._publisher.delete_topic(self._topic_path)
            print("Deleted topic " + self._topic_path)
        except:
            pass


def exists(rest_type, **param):
    """
    Check if a google REST object exists.

    :param rest_type: The REST object type to check
    :param param: Parameters to specify the REST object, passed to the GET call.
    :return: True if the REST object exists, or False otherwise
    """
    try:
        rest_type.get(**param).execute()
        return True  # no error
    except googleapiclient.errors.HttpError as err:
        if err.resp.status == 404:
            return False
        else:
            raise err


def delete_if_exists(rest_type, wait: bool = True, **param):
    """
    Delete a google REST object if it exists. If wait is True, wait for the deletion to complete.

    :param rest_type: The REST object type to check
    :param wait: True if we should wait for the deletion to complete before returning.
    :param param: Parameters to specify the REST object, passed to the GET and DELETE calls.
    :return: True if the REST object existed before, and False otherwise
    """
    if exists(rest_type, **param):
        rest_type.delete(**param).execute()
        if wait:
            time.sleep(1)
            while exists(rest_type, **param):
                time.sleep(1)
        return True
    return False


class GCEOperation:
    def __init__(self, compute, op):
        """
        Create a new updatable wrapper around a GCE operation call
        :param compute: The GCE compute API to use
        :param op: The current state of a GCE operation
        """
        self._base = op

        project_match = re.search("/projects/([^/]*)/", op["targetLink"])
        if project_match:
            project_id = project_match.group(1)
        else:
            raise RuntimeError("Unable to detect project from operation", op)

        if "zone" in self._base:
            zone = op["zone"][op["zone"].rfind("/") + 1 :]
            self._refresh_call = compute.zoneOperations().get(
                operation=self._base["name"], project=project_id, zone=zone
            )
        else:
            self._refresh_call = compute.globalOperations().get(
                operation=self._base["name"], project=project_id
            )

    def refresh(self):
        """
        Consult the server to update progress on this operation.
        :return: self, updated
        """
        self._base = self._refresh_call.execute()
        return self

    @property
    def base(self):
        """
        :return: The underlying GCE operation dict
        """
        return self._base

    def wait(self, query_delay=1):
        """
        Wait until an operation is marked as done.

        :param query_delay: Time to wait in between status checks
        :return: None
        """
        if self._base["status"] == "DONE":
            if "error" in self._base:
                raise Exception(self._base["error"])
            return

        while True:
            self.refresh()
            if self._base["status"] == "DONE":
                if "error" in self._base:
                    raise Exception(self._base["error"])
                return
            time.sleep(query_delay)
