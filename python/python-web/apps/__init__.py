#!/usr/bin/python3
#coding=utf-8
# import sys
from flask import Flask,make_response,request,redirect,url_for
from flask_cors import *
# from .database import db
# from flask_sqlalchemy import SQLAlchemy

# sys.path.append('.')

# app = Flask(__name__,static_folder='mystatic', static_url_path='/myurl',template_folder='mytemplate')
app = Flask(__name__,static_folder='static', static_url_path='/static',template_folder='templates')
app.config.from_object('setting.DevelopmentConfig')
CORS(app, supports_credentials=True)
from .routers import Router
# print('1')
# connMysql(app)
# db.init_app(app)
# print(db)

# print(dir(app))
# print(connMysql)
# db.init_app(app)

# DIALECT = 'mysql'
# DRIVER = 'pymysql'
# USERNAME = 'root'
# PASSWORD = '808069'
# HOST = '127.0.0.1'
# PORT = '3306'
# DATABASE = 'cms'

# SQLALCHEMY_DATABASE_URI = '{}+{}://{}:{}@{}:{}/{}?charset=utf8'.format(
#     DIALECT,DRIVER,USERNAME,PASSWORD,HOST,PORT,DATABASE
# )
# print(SQLALCHEMY_DATABASE_URI)
# db = SQLAlchemy(app)
# print(db)

# print(dir(db))
@app.before_first_request
def before_first_request():
  print("before first request，第一次请求前的操作")
@app.before_request
def before_request():
  # print(request.cookies.get('username'))
  # flag = -1
  # urlList = [
  #   '/user/login',
  #   '/user/loginsubmit',
  #   '/user/loginout'
  # ]
  # try:
  #   flag = urlList.index(request.path)
  # except:
  #   flag = -1
  # # print(flag)
  # if flag==-1 and request.cookies.get('username')==None:
  #   return redirect(url_for('user_index.user_login'))
  print("before request， 每一次请求前都会执行")
  # return 'before'
@app.after_request
def after_request(response):
  response = make_response(response)
  response.headers['Access-Control-Allow-Origin'] = '*'
  response.headers['Access-Control-Allow-Methods'] = 'OPTIONS,HEAD,GET,POST'
  response.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type'
  print("after request，加工响应对象")
  return response
@app.teardown_request
def teardown_request(e):
  print("teardown_request, 请求之后一定执行")
  # print(e)

Router(app)
