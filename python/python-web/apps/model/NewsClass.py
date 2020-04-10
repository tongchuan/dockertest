#!/usr/bin/python3
#coding=utf-8
from datetime import datetime 
from ..database import db
from .Base import Base
class NewsClass(Base,db.Model):
    __tablename__ = 'news_class'
    id = db.Column(db.Integer, primary_key=True,unique=True,index=True) # 'ID',
    title = db.Column('title',db.String(100),nullable=True) # 'title',
    keywork = db.Column(db.String(200),nullable=True) #'关键字',
    description = db.Column(db.String(500),nullable=True) #'描述',
    addtime = db.Column(db.DateTime(),default=datetime.now) #'添加时间',
    updatetime = db.Column(db.DateTime(),default=datetime.now) #'修改时间',
    deletetime = db.Column(db.DateTime(),default=datetime.now) #'删除时间',
    order = db.Column(db.Float(),default=1) #'排序',
    code = db.Column(db.String(32),unique=True,nullable=True) #'编码',
    name = db.Column(db.String(200),nullable=True) #'名称',
    pinyinname = db.Column(db.String(200),nullable=True) #'名称拼音',
    cnname = db.Column(db.String(200),nullable=True) # '中文名称预留',
    enname = db.Column(db.String(200),nullable=True) #'英文名称',
    color = db.Column(db.String(200),nullable=True) #'名称颜色',
    classname = db.Column(db.String(1000),nullable=True) #'class名',
    style = db.Column(db.Unicode(2000),nullable=True) #'样式',
    link = db.Column(db.String(1000),nullable=True) #'链接地址',
    author = db.Column(db.String(200),nullable=True) #'添加或修改人',
    image = db.Column(db.String(1000),nullable=True) #'图片地址',
    smallimage = db.Column(db.String(1000),nullable=True) #'小图片地址',
    bigimage = db.Column(db.String(1000),nullable=True) #'大图片地址',
    desc = db.Column(db.Text,nullable=True) #'说明',
    isdefault = db.Column(db.Boolean(),default=False) #'是否默认',
    ishot = db.Column(db.Boolean(),default=False) #'是否热点',
    isstatic = db.Column(db.Boolean(),default=False) #'是否静态',
    isdelete = db.Column(db.Boolean(),default=False) #'是否删除',
    isrecommend = db.Column(db.Boolean(),default=False) #'是否推荐',
    count = db.Column(db.BigInteger(),default=0) #'点击数量',
    pcode = db.Column(db.String(32),unique=True,nullable=True) #'父编码',
    # def __init__(self):
    #   pass
    #     # self.code = code
    #     # self.name = name
    #     # self.link = link
    # def __repr__(self):
    #     return '<NewsClass %r>' % self.id
