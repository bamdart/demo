#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

import requests

import pyfiglet

import bottle
from bottle import default_app, request, route, response, get

# bottle.debug(True)

@get('/')
def index():
    response.content_type = 'text/plain; charset=utf-8'
    return pyfiglet.figlet_format('Hello, Bottle')

@get('/<name>')
def greet(name):
    response.content_type = 'text/plain; charset=utf-8'
    return pyfiglet.figlet_format('Hello, %s' % name)

@get('/418')
def my418():
    r = requests.get('http://httpbin.org/status/418')
    response.content_type = 'text/plain'
    return r.text


app = default_app()
if __name__ == '__main__':
    bottle.run(host='0.0.0.0', port=8080,server="cherrypy")
