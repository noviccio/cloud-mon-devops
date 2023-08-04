#import psutil, which provides functions for retrieving
#information about the system, such as CPU and memory utilization.
#imports Flask class, which is used to create the Flask application,
#and render_template, which is used to render HTML templates.

import psutil
from flask import Flask, render_template

app = Flask(__name__) #creates new Flask application instance 

@app.route("/")
def index():
    cpu_percent = psutil.cpu_percent()
    mem_percent = psutil.virtual_memory().percent 
    Message = None 
    if cpu_percent > 80 or mem_percent > 80:
        Message = "High CPU or Memory Utilization detected. Please scale up" #sends warning message
    return render_template("index.html", cpu_metric=cpu_percent, mem_metric=mem_percent, message=Message) #


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0') #allows web app to be accessible externally, using localhost