from flask import Flask, render_template, redirect, request, Response
from pymongo import MongoClient

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
    
@app.route('/<shortKey>')
def get(shortKey):
    return redirect(MongoClient("mongodb://localhost:27017/")["URLdb"]["URLs"].find_one({"shortKey": shortKey})["site"])

@app.post('/')
def post():
    MongoClient("mongodb://localhost:27017/")["URLdb"]["URLs"].insert_one(request.get_json())
    return Response("URL is been successfully inserted")
    
