from flask import Flask, render_template, request , flash , Markup , send_file
import flask
import os
import shutil
import csv
from fpdf import FPDF
import datetime
from datetime import datetime
from datetime import date
import helper
import helper2
app = Flask(__name__)

def storer():
    if(os.path.exists("files")):
        shutil.rmtree("files")
    else:
        pass
    os.mkdir("files")
    if(os.path.exists("files1")):
        shutil.rmtree("files1")
    else:
        pass
    os.mkdir("files1")
    if(os.path.exists("files2")):
        shutil.rmtree("files2")
    else:
        pass
    os.mkdir("files2")
    if(os.path.exists("./templates/output")):
        shutil.rmtree("./templates/output")
    else:
        pass
    os.mkdir("./templates/output")
    if(os.path.exists("generated")):
        shutil.rmtree("generated")
    else:
        pass
    os.mkdir("generated")

def storer_1():
        if(os.path.exists("./templates/output")):
            shutil.rmtree("./templates/output")
        else:
            pass
        os.mkdir("./templates/output")
        if(os.path.exists("generated")):
            shutil.rmtree("generated")
        else:
            pass
        os.mkdir("generated")

app.secret_key = b'Roopeshwar@333333'

@app.route("/Range" ,methods=['POST' , "GET"])
def generate_marksheet():
    return helper.function_1()

@app.route('/')
def get():
    return render_template('index.html')

@app.route("/all" , methods=["POST","GET"])
def generate_all_sheets():
    if flask.request.method=='POST':
        storer_1()

    helper2.function_2()
    return render_template("index.html")



@app.route("/data" , methods=["POST", "GET"])
def data():
    storer()
    if flask.request.method == 'POST':
        return helper.function()



if __name__ == '__main__':
    app.run(debug=True)


