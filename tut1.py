from flask import Flask, redirect, url_for, render_template, request
import pandas as pd
import csv

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")
 
@app.route("/login", methods=["POST","GET"])
def login():
    if request.method == "POST": # should be capital here!!!!!!!!!!!!!
        user = request.form["nme"]
        return redirect(url_for("user", usr=user))
    else:
        return render_template("login.html")
    
    
@app.route("/<data>", methods=["POST","GET"])
def data(data):
    if request.method == "POST": # should be capital here!!!!!!!!!!!!!
        f = request.form["csvfile"]
        dat =[]
        with open(f) as file:
            csvfile =  csv.reader(file)
            for row in csvfile:
                dat.append(row)
                
        data= pd.DataFrame(dat)
        #print(data)
        data = data.to_html(header=False, index=False)
        return f"{data}"
    else:
        return render_template("data.html", data = data)

@app.route("/<usr>")
def user(usr):
    return f"<h1>{usr}</h1>"



if __name__ == "__main__":
    app.run() 
    #from waitress import serve
    #serve(app, host="0.0.0.0", port=8080)
    
    