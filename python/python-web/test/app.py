#!/usr/bin/python3
#coding=utf-8
import os
from flask import Flask,current_app

app = Flask(__name__)
# app.config.from_object('setting.ProductionConfig')
app.config.from_object('setting.DevelopmentConfig')
@app.route('/')
def index():
  print(app.config['DB_SERVER'])
  print(app.config['DATABASE_URI'])
  print(current_app.config.get('DATABASE_URI'))
  print(os.urandom(24))
  return 'Hello, World!1a'

if __name__=="__main__":
  # app.host='0.0.0.0'
  # app.port='89898'
  app.run(host=app.config['HOST'],port=app.config['PROT'],debug=app.config['DEBUG'])
  # app.run('0.0.0.0',8989,debug=True)
