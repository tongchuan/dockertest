#!/usr/bin/python3
#coding=utf-8

from ..database import db

class Base():
  @staticmethod
  def dropTable():
    db.drop_all()
  @staticmethod
  def createTable():
    db.create_all()
  @staticmethod
  def add(model):
    # try:
      db.session.add(model)
      db.session.commit()
    # except:
      db.session.rollback()
      # return False
    # else:
      # return True
  @staticmethod
  def delete(model):
    try:
      db.session.delete(model)
      db.session.commit()
    except:
      db.session.rollback()
      return False
    else:
      return True
  @staticmethod
  def querall(model):
    return db.session.query(model).filter().all()
  @staticmethod
  def querpage(model,page,per_page):
    max_per_page=None
    error_out=False
    # page 查询的页数
    # per_page 每页的条数
    # max_per_page 每页最大条数，有值时，per_page 受它影响
    # error_out 当值为 True 时，下列情况会报错
    # 当 page 为 1 时，找不到任何数据
    # page 小于 1，或者 per_page 为负数
    # page 或 per_page 不是整数
    # 该方法返回一个分页对象 Pagination
    return db.session.query(model).filter_by().paginate(page=page, per_page=per_page,error_out=error_out, max_per_page=max_per_page)
