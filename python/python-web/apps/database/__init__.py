#!/usr/bin/python3
#coding=utf-8
from .. import app
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app,use_native_unicode='utf8')
# def connMysql(app):
#   global db
#   print(2)
#   db = SQLAlchemy(app)
#   print(db)
#   # print(db)
# print(db)