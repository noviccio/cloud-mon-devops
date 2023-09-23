
## Cloud Native Monitoring App

This is a project for a Cloud-native monitoring app, containerized on Docker, Deployed on K8s using AWS. Now, what exactly does this app do? Well, it records your CPU and RAM usage and displays it for you in an aesthethic fashion. 

## Project Status

Currently, this app is not deployed globally anymore to avoid charges on AWS. However the process was documented. 

## Project Screen Shot(s)

#### Example:   
This is the app, fully deployed onto the internet using Kubernetes. 

![VirtualBox_Xubuntu_08_08_2023_17_40_14](https://github.com/noviccio/zodi-gpt/assets/97764462/02a6ea12-d17b-4542-8fe0-18d277617c73)

## Installation and Setup Instructions


#### Example:  

This was a 2 week long project built over the summer going into my Junior year. Project goals included learning the CI/CD pipeline, and how to use DevOps technologies.

A huge problem I ran into was how to configure the nodes policies on AWS. I spent a lot of time reading documentation on how to do this. 

This project commenced with the creation of a Python monitoring application using Flask from the ground up, initially running it locally on port 5000 for development and testing purposes. The next crucial step involved containerizing the application with Docker, which necessitated the creation of a Dockerfile to specify the application's environment. Subsequently, a Docker image was crafted from this Dockerfile, enabling the seamless deployment of the application within a container. 

For scalability and cloud deployment, an Amazon Elastic Container Registry (ECR) was established to host the Docker image, and the image was successfully pushed to the repository. Further cloud integration took place as an Amazon Elastic Kubernetes Service (EKS) cluster was configured along with nodes. Python was leveraged to create Kubernetes Deployments and services, ensuring efficient container orchestration and scalability. 

Lastly, the application was made accessible on the internet through port forwarding and Kubernetes configurations, culminating in a comprehensive project utilizing Flask, Docker, Amazon ECR, Amazon EKS, and Kubernetes to develop a robust, scalable, and monitored web application.



