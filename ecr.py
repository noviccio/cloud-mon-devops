import boto3  #SDK used to create AWS resources, programatically, in the cloud

#set the client as ECR repo
ecr_client = boto3.client('ecr')

#create an ECR repo name 
repository_name = "my-cloud-app-repo"
#make the actual repo
response = ecr_client.create_repository(repositoryName=repository_name)


repository_uri = response ['repository']['repositoryUri']
print(repository_uri)



