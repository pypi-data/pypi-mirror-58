# Turbine
A Python 3 tool to harness the google cloud to run shell scripts. In particular, if you have
1. a docker image, and
2. many independent, idempotent tasks for that image written as shell scripts,

Turbine allows you to run those tasks on many VMs in parallel on GCE. Turbine is a lot like
* [Google Cloud Run](https://cloud.google.com/run/) except you don't need to hit an HTTP endpoint and it supports large machine types and accelerators;
* [Google Cloud Functions](https://cloud.google.com/functions/) except it supports large machine types and accelerators; and
* [Batch on GKE](https://cloud.google.com/kubernetes-engine/docs/how-to/batch/running-job) except I understand it, it is significantly lighter-weight than Kubernetes, and it provides a path for TPU access.

# Installation
For most users, the recommended method to install is via pip:

```
pip install turbine
```

## Dependencies:
* google-cloud-pubsub
* google-cloud-storage
* google-cloud-logging
* google-api-python-client

See [requirements.txt](requirements.txt) for detailed version information, if needed.
