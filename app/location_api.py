from os import path
import json
from app import app
from flask import render_template, jsonify,request
from config import basedir
from models import Film_location
from flask.ext.cors import cross_origin

@app.route('/')
@app.route('/index')
def index():
        return render_template("index.html")


@app.route('/sfinmovies/api/v1/movies',methods=['GET'])
def getmovies():
    print request.args.items()
    print type(request.args.items())
    ret_arr=[{req_param[0]:req_param[1]} for req_param in request.args.items()]
    return jsonify({"request_parameters":ret_arr})

@app.route('/sfinmovies/api/v1/search',methods=['GET'])
@cross_origin(headers=['Content-Type'])
def searchmovies():
    title= request.args.get('title')
    print title
    query=Film_location.query
    query = query.filter(Film_location.title==title)
    movies=query.all()
    movies = map(lambda movie: jsonify_film_location(movie),movies)
    return jsonify({'movies':movies})


def jsonify_film_location(movie_location):
    fields = ['id', 'title', 'year_released', 'location','latitude', 'longitude']
    json_movie={}
    for field in fields:
        fieldValue=getattr(movie_location,field,None)
        if fieldValue is not None:
            json_movie[field]=fieldValue

    return json_movie

