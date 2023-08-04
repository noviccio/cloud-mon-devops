#define base image
FROM python:3.9-slim-buster 

#set working directory for where application will run
WORKDIR /app 

#copy requirements.txt, which contains dependencies 
COPY requirements.txt . 

#download and installs all dependencies
RUN pip3 install --no-cache-dir -r requirements.txt 

#copy app code to working directory
COPY . . 

#set environment veriables for the flask app 
ENV FLASK_RUN_HOST =0.0.0.0 

#expose the port on which the flask app will run
EXPOSE 5000

#start the flask app when the container is run
CMD ["flask", "run"]


