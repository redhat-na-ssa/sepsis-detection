# Sepsis Detection

## Introduction

Sepsis is a major cause of death from infection and represents a substantial 
healthcare burden, accounting for 6.2% of total hospital costs in the United 
States 20111. The estimated annual incidence of sepsis in the United States 
was 751,000 cases (3 cases/1,000 population) and the estimated number of deaths 
was 215,0002. Recent large-scale epidemiological studies showed that the mortality 
rate of sepsis has decreased but its incidence continues to increase3,4. However, 
the true incidence of sepsis is likely to be underestimated.

Patient with suspicious infection
> Definitions for SIRS and qSOFA. SIRS: systemic inflammatory response syndrome; qSOFA: Sequential Organ Failure Assessment; WBC: white blood cell.

![image](images/SIRSvsqSOFA.jpg)

## Project Overview

Develop and deploy a machine learning model to flag patients at risk of being septic or having Sepsis
on Kubeframe, which consists of:

|Function|Solution|
|-|-|
|AI/ML Operations|<Red Hat Products>|
|AI/ML Development|Open Data Hub project|
|Data Storage|Red Hat OpenShift Container Storage|
|Container Platform|Red Hat OpenShift|
|GPU|NVIDIA|
|Infrastructure|HPE EL8000|

Dataset comes from Kaggle (https://www.kaggle.com/maxskoryk/datasepsis) 
- Total size = 11.4MB
- Total patient entries = 36,302
- Total attributes = 41
- Combined data in .CSV format containing Vitals, Labs and Demographics
- Labeled data column 41 "isSepsis" with 0=False 1=True
- Raw data contains both null and non-null values 
- Data types are numeric (float64 and int64)

# Project Lifecycle
## Development
> Data Engineer
1. Data identification 
1. Data exploration / engineering in Jupyter Notebooks
   
> Data Scientists
1. Data transformation
1. Model development in Jupyter Notebooks
1. Model productization in Python

## Operations   
> Application Developer
1. Model serving using ?
1. Model observations using ?
1. Model update using ?

# References
1. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6304323/ 
1. https://www.kaggle.com/maxskoryk/datasepsis

public or private
aicoe-ci
jupyterhub-build-pipeline

quay.io
create organization
create bot account
assign write permissions
k8s secret, download, pass to aicoe-ci team, update secret
edit the aicoe-ci.yaml
- change line 12 organization
- change line 13 project name
- change line 14 to bot name
create tag 
  issues > new release > patch release
Create imagestream (manual / automated with deploy)

MLOps
Automatically deploy notebook images with github projects
Automatically install packages and python
Update JupyterHub spawner with Notebook images
Automation
CI/CD/Pipeline with Tekton
ImageStream


https://github.com/aicoe-aiops/project-template
https://www.operate-first.cloud/users/data-science-workflows/docs/create_and_deploy_jh_image.md
https://www.youtube.com/watch?v=gEwdJ9LAQ2Q
https://massopen.cloud/
