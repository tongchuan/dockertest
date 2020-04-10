#!/usr/bin/python3
#coding=utf-8
from .main import Main
from .newsclass import newsClassIndex
from .news import newsIndex
from .user import userIndex
from .data import dataIndex
from .test import testIndex
def Router(app):
  app.register_blueprint(Main,url_prefix='/')
  app.register_blueprint(newsIndex)
  app.register_blueprint(userIndex)
  app.register_blueprint(newsClassIndex)
  app.register_blueprint(dataIndex)
  app.register_blueprint(testIndex)

  # app.register_blueprint(news_add,url_prefix='/news/add')
# from flask import Blueprint
# from .news import News

# n = News()
# new=Blueprint('news',__name__)

# print(n)
# @new.route('/')
# n.show

