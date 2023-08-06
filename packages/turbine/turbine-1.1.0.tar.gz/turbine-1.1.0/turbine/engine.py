from google.cloud import pubsub
import google.api_core.exceptions
import google.auth.credentials
import googleapiclient.discovery
import googleapiclient.errors
import time
from typing import List, Tuple, NamedTuple


class GCEConfig(NamedTuple):
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

        :param engine_id: A unique identifier for this engine, used as the resource id for the associated topic, subscription, and instance template..
        :param image: The GCE identifier of a docker image to run.
        :param config: GCE configuration information
        """
        self._id = engine_id
        self._image = image
        self._config = config

        self._publisher = pubsub.PublisherClient(
            **{"credentials": self._config.credentials}
        )
        self._topic_path = self._publisher.topic_path(self._config.project_id, self._id)

        self._subscriber = pubsub.SubscriberClient(
            **{"credentials": self._config.credentials}
        )
        self._subscription_path = self._subscriber.subscription_path(
            self._config.project_id, self._id
        )

        self._compute = googleapiclient.discovery.build(
            "compute", "v1", credentials=self._config.credentials
        )

        self._instance_template = "projects/{project_id}/global/instanceTemplates/{id}".format(
            project_id=self._config.project_id, id=self._id
        )

    def prepare_queue(self):
        """
        Prepare the queue to add tasks to this engine.

        :return: None
        """
        try:
            self._publisher.create_topic(self._topic_path)
            print("Created topic " + self._topic_path)
        except google.api_core.exceptions.AlreadyExists:
            raise RuntimeError(
                "Topic {path} already exists. Perhaps it has already been prepared?".format(
                    path=self._topic_path
                )
            ) from None

        try:
            self._subscriber.create_subscription(
                self._subscription_path, self._topic_path, ack_deadline_seconds=60
            )
            print("Created subscription " + self._subscription_path)
        except google.api_core.exceptions.AlreadyExists:
            raise RuntimeError(
                "Subscription {path} already exists. Perhaps it has already been prepared?".format(
                    path=self._subscription_path
                )
            ) from None

    def _vm_specification(
        self,
        machine_type: str,
        preemptible: bool,
        accelerators: List[Tuple[str, int]],
        delete_when_done: bool,
    ):
        """
        Construct a VM specification for a VM that can process tasks given to this engine.

        There is no public API for constructing a container spec (without going through GKE
        or the online console), so this may be fragile.

        :param machine_type: The machine type to use for the specification.
        :param preemptible: True if the VM should be preemptible, otherwise false.
        :param accelerators: A list of (name, count) for each accelerator to be included.
        :param delete_when_done: True if the VM should delete itself when no tasks exist.
        :return: A dictionary representing a VM specification.
        """
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
            "name": self._id,
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
                "labels": {  # This might need to be updated?
                    "container-vm": parent_vm_image
                },
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

        if accelerators is not None:
            template["properties"]["guestAccelerators"] = [
                {"acceleratorType": accelerator[0], "acceleratorCount": accelerator[1]}
                for accelerator in accelerators
            ]
        return template

    def prepare_workers(
        self,
        machine_type: str = "n1-standard-1",
        preemptible: bool = True,
        accelerators: List[Tuple[str, int]] = None,
        delete_when_done: bool = True,
    ):
        """
        Run initial, cheap preparations for an instance group of VMs that can process tasks given to this engine.

        In particular, set up an instance template for such VMs. Delete the previous instance template if any exists.

        :param machine_type: The machine type to use for the specification.
        :param preemptible: True if the VM should be preemptible, otherwise false.
        :param accelerators: A list of (name, count) for each accelerator to be included.
        :param delete_when_done: True if the VM should delete itself when there are no tasks left.
        :return: None
        """

        delete_if_exists(
            self._compute.instanceTemplates(),
            project=self._config.project_id,
            instanceTemplate=self._id,
        )

        template = self._vm_specification(
            machine_type=machine_type,
            preemptible=preemptible,
            accelerators=accelerators,
            delete_when_done=delete_when_done,
        )

        self._compute.instanceTemplates().insert(
            project=self._config.project_id, body=template
        ).execute()

    def add_task(
        self,
        script: str,
        inputs: List[Tuple[str, str]] = None,
        outputs: List[Tuple[str, str]] = None,
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

        self._publisher.publish(self._topic_path, bytes(script, "UTF-8"), **attributes)

    def start_workers(
        self, target_size: int, worker_id: str = "", gcloud: bool = False
    ):
        """
        Start an instance group to process tasks given to this engine. All VMs in the instance group will automatically
        delete themselves when the engine has no tasks left.

        If {gcloud} is true, returns a command to run in gcloud.
        If {gcloud} is false, returns the result of the REST API call to start the instance group.

        I would prefer to only offer the REST API, but the API call currently doesn't work.

        :param target_size: The number of VMs (<=500) to target in the instance group.
        :param worker_id: An additional, optional identifier for this worker. This can be used if a previous worker
                          is already running, or in the process of being deleted.
        :param gcloud: True if a gcloud call should be used instead of the REST API.
        :return: Either a gcloud call to run, or the result of the REST API call.
        """
        if worker_id == "":
            name = self._id
        else:
            name = self._id + "-" + worker_id

        if target_size > 500:
            raise RuntimeError(
                "Maximum allowed target size of 500"
            )  # Otherwise I have to figure out REST pagination

        if gcloud:
            return " ".join(
                [
                    "gcloud compute instance-groups managed create {name}",
                    "--base-instance-name {name}",
                    "--size {size}",
                    "--template {template}",
                    "--zone {zone}",
                    "--project {project}",
                ]
            ).format(
                name=name,
                size=target_size,
                template=self._instance_template,
                zone=self._config.zone,
                project=self._config.project_id,
            )
        else:
            return (
                self._compute.instanceGroupManagers()
                .insert(
                    project=self._config.project_id,
                    zone=self._config.zone,
                    body={
                        "name": name,
                        "instanceTemplate": self._instance_template,
                        "baseInstanceName": name,
                        "targetSize": target_size,
                    },
                )
                .execute()
            )

    def workers(self):
        """
        Find all workers currently running tasks for this engine.
        :return:
        """

        def delete_instance_group_manager(name, wait=True):
            """
            Delete the provided instance group manager in this project
            :param name: The name of the instance group manager to delete.
            :param wait: If true, wait for the instance group manager to be deleted.
            :return: None
            """
            print("Deleting instance group manager " + name)
            delete_if_exists(
                self._compute.instanceGroupManagers(),
                wait=wait,
                project=self._config.project_id,
                zone=self._config.zone,
                instanceGroupManager=name,
            )

        class InstanceGroupWorker:
            def __init__(self, base):
                self._base = base

            def __getitem__(self, name):
                return self._base[name]

            def delete(self, force_stop=False, wait=True):
                """
                Delete the instance group.

                :param force_stop: If False, an exception will be raised if the group still has active workers.
                :param wait: If true, wait for the instance group manager to be deleted.
                :return: None
                """
                if self["targetSize"] > 0 and not force_stop:
                    raise Exception("Instance group {name} has {num} workers running")
                delete_instance_group_manager(self["name"], wait=wait)

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
                if group["instanceTemplate"].endswith(self._instance_template):
                    result.append(InstanceGroupWorker(group))
        return result

    def cleanup_workers(self, force_stop=False, wait=True):
        """
        Delete all workers provisioned by this engine.

        :param force_stop: If False, an exception will be raised if the group still has active workers.
        :param wait: If true, wait for all workers to be deleted.
        :return: None
        """
        for worker in self.workers():
            worker.delete(force_stop=force_stop, wait=wait)

    def cleanup(self, force_stop=True, wait=True):
        """
        Delete all resources provisioned by this engine.

        :param force_stop: If False, an exception will be raised if the group still has active workers.
        :param wait: If true, wait for all workers to be deleted.
        :return: None
        """
        for worker in self.workers():
            worker.delete(force_stop=force_stop, wait=wait)

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
        try:
            self._compute.instanceTemplates().delete(
                project=self._config.project_id, instanceTemplate=self._id
            ).execute()
            print("Deleted instance template " + self._instance_template)
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
