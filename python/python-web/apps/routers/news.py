#!/usr/bin/python3
#coding=utf-8
from flask import Blueprint,render_template
import random
from ..utils.json import jsonDumps,jsonLoads
from ..model.News import News
newsIndex=Blueprint('news_index',__name__)

@newsIndex.route('/news')
def news_index():
  movies = [
    {'name' : 'My Neighbor Totoro','year':'1988'},
    {'name': 'Three Colours trilogy', 'year': '1993'},
    {'name': 'Forrest Gump', 'year': '1994'},
    {'name': 'Perfect Blue', 'year': '1997'},
    {'name': 'The Matrix', 'year': '1999'},
    {'name': 'Memento', 'year': '2000'},
    {'name': 'The Bucket list', 'year': '2007'},
    {'name': 'Black Swan', 'year': '2010'},
    {'name': 'Gone Girl', 'year': '2014'},
    {'name': 'CoCo', 'year': '2017'}]
  return render_template('news/index.html',data={"movies":movies})
  return 'news.index'

@newsIndex.route('/news/add')
def news_add():
  """模拟添加数据"""
  i = 0
  while True:
    i+=1
    if(i>10):
      break
    news1 = News(title='标题'+str(random.randint(100,1000)),code='编码'+str(random.randint(100,1000)),name=str(i)+'我的名字'+str(random.randint(100,1000)))
    News.add(news1)
  return 'news.add'
@newsIndex.route('/news/count')
def news_count():
  '''查询总共有多少条数据'''
  count = News.query.count()
  data = {
    'data': count,
    'message': '查询总数成功！',
    'success': True,
    'code': 1
  }
  return jsonDumps(data)

@newsIndex.route('/news/all')
def news_all():
  '''查询所有数据'''
  data = {
    'data': []
  }
  try:
    queryall = News.query.all()
    for item in queryall:
      data['data'].append({
        'id': item.id,
        'newsclassid': item.newsclassid,
        'title': item.title,
        'keywork': item.keywork,
        'description': item.description,
        'addtime': item.addtime,
        'updatetime': item.updatetime,
        'deletetime': item.deletetime,
        'order': item.order,
        'code': item.code,
        'name': item.name,
        'pinyinname': item.pinyinname,
        'cnname': item.cnname,
        'enname': item.enname,
        'color': item.color,
        'classname': item.classname,
        'style': item.style,
        'link': item.link,
        'author': item.author,
        'image': item.image,
        'smallimage': item.smallimage,
        'bigimage': item.bigimage,
        'desc': item.desc,
        'isdefault': item.isdefault,
        'ishot': item.ishot,
        'isstatic': item.isstatic,
        'isdelete': item.isdelete,
        'isrecommend': item.isrecommend,
        'count': item.count,
      })
  except BaseException:
    data['success'] = False 
    data['code'] = 0 
    data['message'] = '查询数据失败'
  else:
    data['success'] = True 
    data['code'] = 1
    data['message'] = '查询数据成功'
  return jsonDumps(data)

@newsIndex.route('/news/first')
def news_first():
  '''查询第一数据'''
  data = {}
  try:
    item = News.query.first()
    data['data'] = {
        'id': item.id,
        'newsclassid': item.newsclassid,
        'title': item.title,
        'keywork': item.keywork,
        'description': item.description,
        'addtime': item.addtime,
        'updatetime': item.updatetime,
        'deletetime': item.deletetime,
        'order': item.order,
        'code': item.code,
        'name': item.name,
        'pinyinname': item.pinyinname,
        'cnname': item.cnname,
        'enname': item.enname,
        'color': item.color,
        'classname': item.classname,
        'style': item.style,
        'link': item.link,
        'author': item.author,
        'image': item.image,
        'smallimage': item.smallimage,
        'bigimage': item.bigimage,
        'desc': item.desc,
        'isdefault': item.isdefault,
        'ishot': item.ishot,
        'isstatic': item.isstatic,
        'isdelete': item.isdelete,
        'isrecommend': item.isrecommend,
        'count': item.count,
      }
  except BaseException:
    data['success'] = False 
    data['code'] = 0 
    data['message'] = '查询数据失败'
  else:
    data['success'] = True 
    data['code'] = 1
    data['message'] = '查询数据成功'
  return jsonDumps(data)
@newsIndex.route('/news/get/<id>',methods=['get','post'])
def news_get(id):
  '''查询第一数据'''
  data = {}
  try:
    item = News.query.get(id)
    data['data'] = {
        'newsclassid': item.newsclassid,
        'title': item.title,
        'keywork': item.keywork,
        'description': item.description,
        'addtime': item.addtime,
        'updatetime': item.updatetime,
        'deletetime': item.deletetime,
        'order': item.order,
        'code': item.code,
        'name': item.name,
        'pinyinname': item.pinyinname,
        'cnname': item.cnname,
        'enname': item.enname,
        'color': item.color,
        'classname': item.classname,
        'style': item.style,
        'link': item.link,
        'author': item.author,
        'image': item.image,
        'smallimage': item.smallimage,
        'bigimage': item.bigimage,
        'desc': item.desc,
        'isdefault': item.isdefault,
        'ishot': item.ishot,
        'isstatic': item.isstatic,
        'isdelete': item.isdelete,
        'isrecommend': item.isrecommend,
        'count': item.count,
      }
  except BaseException:
    data['success'] = False 
    data['code'] = 0 
    data['message'] = '查询数据失败'
  else:
    data['success'] = True 
    data['code'] = 1
    data['message'] = '查询数据成功'
  return jsonDumps(data)


@newsIndex.route('/news/page')
def news_page():
  """分页查询, 每页3个, 查询第2页的数据"""
  data = {
    'data': []
  }
  # print(len(queryall))
  try:
    page = 1
    per_page = 3
    # queryall = News.query.order_by('id').paginate(page, per_page, error_out=True, max_per_page=None)
    # queryall = News.query.order_by(News.order,News.addtime,News.id.desc()).paginate(page, per_page, error_out=True, max_per_page=None)
    queryall = News.query.filter(News.name.like('%我的名字%'),News.code.like('%1%')).order_by(News.id.asc(),News.order,News.addtime).paginate(page, per_page, error_out=True, max_per_page=None)
    for item in queryall.items:
      data['data'].append({
        'id': item.id,
        'newsclassid': item.newsclassid,
        'title': item.title,
        'keywork': item.keywork,
        'description': item.description,
        'addtime': item.addtime,
        'updatetime': item.updatetime,
        'deletetime': item.deletetime,
        'order': item.order,
        'code': item.code,
        'name': item.name,
        'pinyinname': item.pinyinname,
        'cnname': item.cnname,
        'enname': item.enname,
        'color': item.color,
        'classname': item.classname,
        'style': item.style,
        'link': item.link,
        'author': item.author,
        'image': item.image,
        'smallimage': item.smallimage,
        'bigimage': item.bigimage,
        'desc': item.desc,
        'isdefault': item.isdefault,
        'ishot': item.ishot,
        'isstatic': item.isstatic,
        'isdelete': item.isdelete,
        'isrecommend': item.isrecommend,
        'count': item.count,
      })
  except BaseException:
    data['success'] = False 
    data['code'] = 0 
    data['message'] = '查询数据失败'
  else:
    data['success'] = True 
    data['code'] = 1
    data['message'] = '查询数据成功'
  return jsonDumps(data)


# @news.route('/')
# class News(object):
#   def show():
#     return 'news.show'

# def show():
#   print(news)
#   print(__name__)
#   return 'news.hello'