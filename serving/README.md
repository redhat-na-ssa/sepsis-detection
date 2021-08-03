# Sepsis Detection As a Serverless API

Instructions to deploy the sepsis-detection as a serverless function on OpenShit

## To just deploy to Openshift

To deploy and test on OpenShift

1. Install OCP Serverless Operator from OperatorHub
1. Install Knative Serving from Installed Operators under project: knative-serving

```sh
git clone https://github.com/redhat-naps-da/sepsis-detection.git
cd serving
oc project sepsis-detection
oc apply -f fn/kubernetes/
```

This will create a knative service using. The minimum number of pods is set to 1 (not zero) due to performance loading the model and pipeline each time from zero versus having at least 1 pod with the model and pipeline loaded

```yaml
spec:
  template:
    metadata:
      annotations:
        autoscaling.knative.dev/minScale: '1'
```

Alternatively, you can use the kn CLI

```
kn service create sepsis-detection --port 8080 --image quay.io/redhat_naps_da/sepsis-detection:latest --scale-min 1 --scale-max 10 --label app.openshift.io/runtime=python
```

Or use the +Add Wizard on the OpenShift Developer console. Select Container Image and enter `quay.io/redhat_naps_da/sepsis-detection:latest` as the image. For the Resource, select Knative Service. You also have the option to deploy it as a regular Kubernetes Deployment (or OpenShift DeploymentConfig), however, the service will lack the serverless capabilities. 

to test with `curl`
```
    KROUTE=$(oc get route.serving.knative.dev/sepsis-detection --template='{{ .status.url }}' )
    
    # if using Deployment or DeploymentConfig, get the url using the OpenShift route
    # KROUTE=$(oc get route  sepsis-detection --template='{{ .spec.host }}' )
    
 

 curl -X POST -H "Content-Type: application/json" --data '{"HR":103,"O2Sat":90,"Temp":null,"SBP":null,"MAP":null,"DBP":null,"Resp":30,"EtCO2":null,"BaseExcess":21,"HCO3":45,"FiO2":null,"pH":7.37,"PaCO2":90,"SaO2":91,"AST":16,"BUN":14,"Alkalinephos":98,"Calcium":9.3,"Chloride":85,"Creatinine":0.7,"Glucose":193,"Lactate":null,"Magnesium":2,"Phosphate":3.3,"Potassium":3.8,"Bilirubin_total":0.3,"Hct":37.2,"Hgb":12.5,"PTT":null,"WBC":5.7,"Fibrinogen":null,"Platelets":317}' $KROUTE


 curl -X POST -H "Content-Type: application/json" --data '{"HR":72.0,"O2Sat":96.0,"Temp":null,"SBP":103.0,"MAP":62.0,"DBP":45.0,"Resp":20.0,"EtCO2":null,"BaseExcess":-1.0,"HCO3":null,"FiO2":null,"pH":7.4,"PaCO2":36.0,"SaO2":98.0,"AST":null,"BUN":null,"Alkalinephos":null,"Calcium":null,"Chloride":null,"Creatinine":null,"Glucose":null,"Lactate":null,"Magnesium":null,"Phosphate":null,"Potassium":null,"Bilirubin_total":null,"Hct":null,"Hgb":null,"PTT":null,"WBC":null,"Fibrinogen":null,"Platelets":null}' $KROUTE
```

## To test locally and deploy using OpenShift Serverless Functions

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

   `$ kn func create serving/fn2 -r quay.io -l python -t http -i /redhat_naps_da/sepsis-detection:latest -n sepsis-detection`

   The image name can be modified in func.yaml
1. To run the unit tests locally

   `$ pip3 install -r requirements.txt` 

   `$ python3 test_func.py` 
1. To build the function image locally

   `$ kn func build` 

   To build a different image name or version from the one specified in func.yaml

   `$ kn func build -i <image-name>:<image-version>` 

   Note that this will modify the name of the image in func.yaml

   you can also push to an external registry like quay.io using podman or docker. All `podman` commands below work with `docker`

   `$ podman push <image-name-specified-in-func.yaml>`

1. To build the function with OCP Container Registry

   `$ kn func build -r $(oc get route -n openshift-image-registry)`


1. Test the function locally

   `$ kn func run`   
    The container could also be run from directly from `podman` (especially if you want to run another version)
    ```
    podman run --rm --name=sepsis-detection -p8080:8080 -d <image-name>:<image-version>
    ```
    Test locally by sending data with a `curl`.

    ```
    curl -X POST -H "Content-Type: application/json" --data '{"HR":103,"O2Sat":90,"Temp":null,"SBP":null,"MAP":null,"DBP":null,"Resp":30,"EtCO2":null,"BaseExcess":21,"HCO3":45,"FiO2":null,"pH":7.37,"PaCO2":90,"SaO2":91,"AST":16,"BUN":14,"Alkalinephos":98,"Calcium":9.3,"Chloride":85,"Creatinine":0.7,"Glucose":193,"Lactate":null,"Magnesium":2,"Phosphate":3.3,"Potassium":3.8,"Bilirubin_total":0.3,"Hct":37.2,"Hgb":12.5,"PTT":null,"WBC":5.7,"Fibrinogen":null,"Platelets":317}' http://127.0.0.1:8080
    ```

    ```
    curl -X POST -H "Content-Type: application/json" --data '{"HR":72.0,"O2Sat":96.0,"Temp":null,"SBP":103.0,"MAP":62.0,"DBP":45.0,"Resp":20.0,"EtCO2":null,"BaseExcess":-1.0,"HCO3":null,"FiO2":null,"pH":7.4,"PaCO2":36.0,"SaO2":98.0,"AST":null,"BUN":null,"Alkalinephos":null,"Calcium":null,"Chloride":null,"Creatinine":null,"Glucose":null,"Lactate":null,"Magnesium":null,"Phosphate":null,"Potassium":null,"Bilirubin_total":null,"Hct":null,"Hgb":null,"PTT":null,"WBC":null,"Fibrinogen":null,"Platelets":null}' http://127.0.0.1:8080

    ```

1. Deploy the function to OpenShift

   `$ kn func deploy`   

   to test with `curl`
   ```
   KROUTE=$(oc get route.serving.knative.dev/sepsisfunction --template='{{ .status.url }}' )

    curl -X POST -H "Content-Type: application/json" --data '{"HR":103,"O2Sat":90,"Temp":null,"SBP":null,"MAP":null,"DBP":null,"Resp":30,"EtCO2":null,"BaseExcess":21,"HCO3":45,"FiO2":null,"pH":7.37,"PaCO2":90,"SaO2":91,"AST":16,"BUN":14,"Alkalinephos":98,"Calcium":9.3,"Chloride":85,"Creatinine":0.7,"Glucose":193,"Lactate":null,"Magnesium":2,"Phosphate":3.3,"Potassium":3.8,"Bilirubin_total":0.3,"Hct":37.2,"Hgb":12.5,"PTT":null,"WBC":5.7,"Fibrinogen":null,"Platelets":317}' $KROUTE


    curl -X POST -H "Content-Type: application/json" --data '{"HR":72.0,"O2Sat":96.0,"Temp":null,"SBP":103.0,"MAP":62.0,"DBP":45.0,"Resp":20.0,"EtCO2":null,"BaseExcess":-1.0,"HCO3":null,"FiO2":null,"pH":7.4,"PaCO2":36.0,"SaO2":98.0,"AST":null,"BUN":null,"Alkalinephos":null,"Calcium":null,"Chloride":null,"Creatinine":null,"Glucose":null,"Lactate":null,"Magnesium":null,"Phosphate":null,"Potassium":null,"Bilirubin_total":null,"Hct":null,"Hgb":null,"PTT":null,"WBC":null,"Fibrinogen":null,"Platelets":null}' $KROUTE
    ```


Reference
1. [serverless-functions](https://access.redhat.com/documentation/en-us/openshift_container_platform/4.7/html/serverless/functions#serverless-functions-about)
