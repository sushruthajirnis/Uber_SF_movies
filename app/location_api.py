from os import path
import json
from app import app
from flask import render_template, jsonify
from config import basedir


@app.route('/')
@app.route('/index')
def index():
        return render_template("index.html")


@app.route('/sfinmovies/api/movies',methods=['GET'])
def getmovies():
    filePath =path.join(basedir,"data","yitu-d5am.json")
    fileInp=open(filePath,'r')
    movies = json.load(fileInp)
    fileInp.close()
    return jsonify({"movie_list":movies})
