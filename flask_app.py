# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 15:22:02 2021

@author: shiri
"""

import flask
from flask import Flask,redirect, url_for, request,render_template,send_file,jsonify

import werkzeug
import pandas as pd
from werkzeug.utils import secure_filename

global d,d1
global labs,lablist


app=Flask(__name__)

@app.route("/")
def flames():
    return render_template("flamesup.html")

@app.route("/flamescode",methods=["POST"]) 
def flamescode():
    if(request.method=="POST"):
        n=request.form["first"]
        m=request.form["last"]
    l=[]

    if(len(m)>len(n)):
        x=list(m)
        y=list(n)
    else:
        x=list(n)
        y=list(m)
    print(l)
    exp=[]
    k=0
    for i in range(len(x)):
        for j in range(len(y)):
            if(x[i]==y[j] and i not in exp and j not in exp):
                exp.extend([i,j])
                k+=2
    l=len(x)+len(y)-k
    print(l)
    code=list("flames")
    while(len(code)!=1):
        ind=(l-1)%len(code)
        temp=code[ind+1:]
        code=code[:ind]
        temp.extend(code)
        code=temp
    d={"f":"Friends","l":"Lovers","a":"Affectionate","m":"Marriage","e":"Enemies","s":"Siblings"}
    return render_template("flamesup.html", submitted=True,value=d[code[0]])

if __name__ == '__main__':
   app.run()