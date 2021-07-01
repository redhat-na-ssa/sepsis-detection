# Serving

OpenShift Serverless Python Function
- OpenShift Serverless Functions enables developers to create and deploy stateless, event-driven functions as a Knative service on OpenShift Container Platform.

End to End [Serverless Python Function](https://access.redhat.com/documentation/en-us/openshift_container_platform/4.7/html/serverless/functions#serverless-developing-python-functions)
1. Install OCP Serverless Operator from OperatorHub
1. Install Knative Serving from Installed Operators under project: knative-serving
1. Install Knative Eventing from Installed Operators under project: knative-eventing
1. Install `oc` CLI
1. Install `kn func` CLI plugin
1. Install `podman` or `Docker Container Engine`
    1. Set podman to listen on port 1234
        `$ podman system service --time=0 tcp:0.0.0.0:1234 & # let run in background or another terminal`
    1. Establish the environment variable that is used to build a function
        `$ export DOCKER_HOST=tcp://127.0.0.1:1234`
1. [Expose the OpenShift registry](https://access.redhat.com/documentation/en-us/openshift_container_platform/4.7/html-single/registry/index#securing-exposing-registry)
    1. Deploy Registry Operator
    1. Deploy Ingress Operator
    1. Set `DefaultRoute` to `True`
        `$ HOST=$(oc get route default-route -n openshift-image-registry --template='{{ .spec.host }}')`
    1. Login with Podman
        `$ HOST=$(oc get route default-route -n openshift-image-registry --template='{{ .spec.host }}')`
    1. --tls-verify=false is needed if the cluster’s default certificate for routes is untrusted. You can set a custom, trusted certificate as the default certificate with the Ingress Operator.    
        `$ podman login -u kubeadmin -p $(oc whoami -t) --tls-verify=false $HOST`
    1. Search for python images
        `$ podman search --filter=is-official --limit 3 python`
1. Create the python function
   `$ kn func create <path> -r registry.redhat.io -l python -t http -i /ubi8/python-38 -n sepsisdetection`
1. Build the function with OCP Container Registry
   `$ kn func build -r $(oc get route -n openshift-image-registry)`
1. Deploy the function   
   `$ kn func deploy -r $(oc get route -n openshift-image-registry)`   
   


Reference
1. [serverless-functions](https://access.redhat.com/documentation/en-us/openshift_container_platform/4.7/html/serverless/functions#serverless-functions-about)