from bottle import Bottle, run, route, static_file, request, response, template
from pymongo import MongoClient
from bson.json_util import dumps
from string import Template
import json
import pymongo
import requests
import datetime
import time
import urlparse
import hashlib
import os

app = Bottle(__name__)

client = MongoClient()
db = client.bae_chat

@app.route('/')
def root():
	return static_file('index.html', root='templates/')

@app.route('/kid-profile')
def root():
	return static_file('kid_profile.html', root='templates/')

@app.route('/post')
def root():
	return static_file('post.html', root='templates/')

@app.route('/privacy-policy')
def privacy_policy():
	return static_file('privacy-policy.html', root='templates/')

@app.route('/terms-of-service')
def terms_of_service():
	return static_file('terms-of-service.html', root='templates/')



# Static Routes
@app.route('/<filename:re:.*\.js>')
def javascripts(filename):
    return static_file(filename, root='static')

@app.route('/<filename:re:.*\.css>')
def stylesheets(filename):
    return static_file(filename, root='static')

@app.route('/<filename:re:.*\.(jpg|png|gif|ico|svg)>')
def images(filename):
    return static_file(filename, root='static')

@app.route('/<filename:re:.*\.(eot|ttf|woff|svg)>')
def fonts(filename):
    return static_file(filename, root='static')

@app.hook('after_request')
def enable_cors():
	response.headers['Access-Control-Allow-Origin'] = '*'
	response.headers['Access-Control-Allow-Methods'] = 'PUT, GET, POST, DELETE, OPTIONS'
	response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'