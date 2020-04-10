#!/usr/bin/python3
#coding=utf-8
from flask import Blueprint,render_template
from ..database import db
dataIndex=Blueprint('data_index',__name__)
# print(dir(News))
@dataIndex.route('/data')
def data_index():
  return 'db'

@dataIndex.route('/data/create')
def data_create():
  db.create_all()
  return 'db.create_all'

@dataIndex.route('/data/drop')
def data_drop():
  db.drop_all()
  return 'db.drop_all'
  # return 'main'
