#!/usr/bin/python3
#coding=utf-8
from datetime import datetime 
from .Base import Base
from ..database import db

class User(Base,db.Model):
  __tablename__='user'
  id=db.Column('id',db.Integer,primary_key=True,autoincrement=True)
  name=db.Column('username',db.String(50),nullable=True,unique=True)
  pwd=db.Column('password',db.String(50),nullable=True)
  email = db.Column(db.String(64), unique=True, index=True)
  sort=db.Column(db.Integer)
  addtime = db.Column('add_time',db.DateTime(),default=datetime.now)
  def __init__(self):
    pass
  def queryByNameAndPwd(self):
    print(self.name)
    return db.session.query(self).filter().all()
  def __repr__(self):
    return '<User %r>' % self.name