#!/usr/bin/python3
#coding=utf-8
from flask import Blueprint,render_template,request
from ..utils.json import jsonDumps,jsonLoads
from ..model.NewsClass import NewsClass



newsClassIndex=Blueprint('news_class_index',__name__)

@newsClassIndex.route('/newsclass')
def news_class_index():
  all_results = NewsClass.querall(NewsClass)
  print(len(all_results))
  return 'news.class.index'

@newsClassIndex.route('/newsclass/add',methods=['POST','GET'])
def news_add():
  # data1 = request.get_data(as_text=True)
  # data2 = request.get_data()
  # data3 = json.loads(data1)
  # print(data1,data2)
  # print(list(data3.keys()))
  data = jsonLoads()
  for item in data['data']:
    newsclass = NewsClass()
    newsclass.title = item['title'] if 'title' in item else None
    newsclass.keywork = item['keywork'] if 'keywork' in item else None
    newsclass.description = item['description'] if 'description' in item else None
    newsclass.addtime = item['addtime'] if 'addtime' in item else None
    newsclass.updatetime = item['updatetime'] if 'updatetime' in item else None
    newsclass.deletetime = item['deletetime'] if 'deletetime' in item else None
    newsclass.order = item['order'] if 'order' in item else None
    newsclass.code = item['code'] if 'code' in item else None
    newsclass.name = item['name'] if 'name' in item else None
    newsclass.pinyinname = item['pinyinname'] if 'pinyinname' in item else None
    newsclass.cnname = item['cnname'] if 'cnname' in item else None
    newsclass.enname = item['enname'] if 'enname' in item else None
    newsclass.color = item['color'] if 'color' in item else None
    newsclass.classname = item['classname'] if 'classname' in item else None
    newsclass.style = item['style'] if 'style' in item else None
    newsclass.link = item['link'] if 'link' in item else None
    newsclass.author = item['author'] if 'author' in item else None
    newsclass.image = item['image'] if 'image' in item else None
    newsclass.smallimage = item['smallimage'] if 'smallimage' in item else None
    newsclass.bigimage = item['bigimage'] if 'bigimage' in item else None
    newsclass.desc = item['desc'] if 'desc' in item else None
    newsclass.isdefault = item['isdefault'] if 'isdefault' in item else None
    newsclass.ishot = item['ishot'] if 'ishot' in item else None
    newsclass.isstatic = item['isstatic'] if 'isstatic' in item else None
    newsclass.isdelete = item['isdelete'] if 'isdelete' in item else None
    newsclass.isrecommend = item['isrecommend'] if 'isrecommend' in item else None
    newsclass.count = item['count'] if 'count' in item else None
    newsclass.pcode = item['pcode'] if 'pcode' in item else None
    # for key in list(item.keys()):
    #   nc[key] = item[key]
    NewsClass.add(newsclass)
    #   print(item[key])
    # print(item['name'])
  # print(len(data['data']))
  # return "{}"
  # for key in list(data3.keys):
  #   print(key)
  # print(data3)
  # print(data3.keys)
  # print(json.loads(data2.decode('utf-8')))
  source = {}
  source['list'] = []
  source['success'] = True
  source['message'] = '查询成功'
  alllist = NewsClass.querall(NewsClass)
  for newsclass in alllist:
    source['list'].append({
      'title': newsclass.title,
      'keywork': newsclass.keywork,
      'description': newsclass.description,
      'addtime': newsclass.addtime,
      'updatetime': newsclass.updatetime,
      'deletetime': newsclass.deletetime,
      'order': newsclass.order,
      'code': newsclass.code,
      'name': newsclass.name,
      'pinyinname': newsclass.pinyinname,
      'cnname': newsclass.cnname,
      'enname': newsclass.enname,
      'color': newsclass.color,
      'classname': newsclass.classname,
      'style': newsclass.style,
      'link': newsclass.link,
      'author': newsclass.author,
      'image': newsclass.image,
      'smallimage': newsclass.smallimage,
      'bigimage': newsclass.bigimage,
      'desc': newsclass.desc,
      'isdefault': newsclass.isdefault,
      'ishot': newsclass.ishot,
      'isstatic': newsclass.isstatic,
      'isdelete': newsclass.isdelete,
      'isrecommend': newsclass.isrecommend,
      'count': newsclass.count,
    })
  return jsonDumps(source)
  # return json.dumps(source,ensure_ascii=False, cls=DateEncoder)
  # return 'news.add'

# @news.route('/')
# class News(object):
#   def show():
#     return 'news.show'

# def show():
#   print(news)
#   print(__name__)
#   return 'news.hello'