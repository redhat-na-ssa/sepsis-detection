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
1. The python function template was created using the following command

   `$ kn func create -r quay.io -l python -t http -i /redhat_naps_da/sepsis-detection:latest -n sepsis-detection`

   The image name can be modified in func.yaml
1. To run the unit tests locally

   `$ pip3 install -r requirements.txt` 

   `$ python3 test_func.py` 
1. To build the function image locally

   `$ kn func build` 
1. To build the function with OCP Container Registry

   `$ kn func build -r $(oc get route -n openshift-image-registry)`

   you can also push to an external registry like quay.io using podman or docker

   `$ podman push <image-name-specified-in-func.yaml>`
1. Test the function locally

   `$ kn func run`   
    The container could also be run from directly from `podman`.
    ```
    podman run --rm --name=sepsis-detection -p8080:8080 -d <image-name-specified-in-func.yaml>
    ```
    Test locally by sending data with a `curl`.

    ```
    curl -X POST -H "Content-Type: application/json" --data "data=@no_sepsis.json" http://127.0.0.1:8080
    ```
    ```
    curl -X POST -H "Content-Type: application/json" --data "data=@sepsis.json" http://127.0.0.1:8080
    ```

1. Deploy the function to OpenShift

   `$ kn func deploy`   
   


Reference
1. [serverless-functions](https://access.redhat.com/documentation/en-us/openshift_container_platform/4.7/html/serverless/functions#serverless-functions-about)