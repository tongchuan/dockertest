#!/usr/bin/python3
#coding=utf-8
from flask import Blueprint,render_template
from .. import app
from flask_sqlalchemy import SQLAlchemy
from ..model.News import News
# db = SQLAlchemy(app)
Main=Blueprint('main',__name__)
# print(dir(News))
@Main.route('/')
def main():
  # db = SQLAlchemy()
  # return str(dir(db))
  # db.init_app(app)
  # return str(app.config['SQLALCHEMY_DATABASE_URI'])
  # return dir(SQLAlchemy)
  # return app.config['SQLALCHEMY_DATABASE_URI']
  
  # db = SQLAlchemy(app,use_native_unicode='utf8')
  return render_template('main.html')
  return 'main'