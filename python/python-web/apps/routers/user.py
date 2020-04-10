#!/usr/bin/python3
#coding=utf-8
from flask import Blueprint,render_template,request,redirect,url_for,Response,make_response
from datetime import datetime,timedelta
# from datetime import 
import json
from ..model.User import User
userIndex=Blueprint('user_index',__name__)
"""
    查询所有用户数据
    User.query.all()

    查询有多少个用户
    User.query.count()

    查询第1个用户
    User.query.first()
    User.query.get(1)   # 根据id查询

    查询id为4的用户[3种方式]
    User.query.get(4)
    User.query.filter_by(id=4).all()   # 简单查询  使用关键字实参的形式来设置字段名
    User.query.filter(User.id == 4).all()  # 复杂查询  使用恒等式等其他形式来设置条件

    查询名字结尾字符为g的所有用户[开始 / 包含]
    User.query.filter(User.name.endswith("g")).all()
    User.query.filter(User.name.startswith("w")).all()
    User.query.filter(User.name.contains("n")).all()
    User.query.filter(User.name.like("%n%g")).all()  模糊查询

    查询名字和邮箱都以li开头的所有用户[2种方式]
    User.query.filter(User.name.startswith("li"), User.email.startswith("li")).all()

    from sqlalchemy import and_
    User.query.filter(and_(User.name.startswith("li"), User.email.startswith("li"))).all()

    查询age是25 或者 `email`以`itheima.com`结尾的所有用户
    from sqlalchemy import or_
    User.query.filter(or_(User.age == 25, User.email.endswith("itheima.com"))).all()

    查询名字不等于wang的所有用户[2种方式]
    from sqlalchemy import not_
    User.query.filter(not_(User.name == "wang")).all()
    User.query.filter(User.name != "wang").all()

    查询id为[1, 3, 5, 7, 9]的用户
    User.query.filter(User.id.in_([1, 3, 5, 7, 9])).all()

    所有用户先按年龄从小到大, 再按id从大到小排序, 取前5个
    User.query.order_by(User.age, User.id.desc()).limit(5).all()

    分页查询, 每页3个, 查询第2页的数据
    pn = User.query.paginate(2, 3)
    pn.items  获取该页的数据     pn.page   获取当前的页码     pn.pages  获取总页数
"""


@userIndex.route('/user')
def user_index():
  # User.createTable()
  data = {}
  try:
    # user = User()
    # user.name = '张彤川'
    # user.pwd='123456'
    # user.email = 'sddsd@as.com'
    # flag = User.add(user)
    # if flag==False :
    #   raise Exception('添加失败')
    for i in range(1):
      user = User()
      user.name = 'zhangtongchuan'
      user.pwd='123456'
      user.email = 'tongchanxing@163.com'
      flag = User.add(user)
      if flag==False :
        raise Exception('添加失败')
        print(i)
        break
  except BaseException:
  # finally:

    data['success'] = False 
    data['message'] = '添加数据失败'
    # return 'abc'
  else:
    data['success'] = True 
    data['message'] = '添加数据成功'
    # return 'bad'
  print(json.dumps(data))
  return json.dumps(data,skipkeys=False, ensure_ascii=False, check_circular=True, allow_nan=True, cls=None, indent=None, separators=None)
  # return 'user.index'
@userIndex.route('/user/querall',methods=['POST','GET'])
def user_all():
  # User.createTable()
  datalist = [] 
  data = {}
  all_results = User.querall(User)
  for user in all_results:
    datauser={
      'name': user.name,
      'password': user.pwd,
      'email': user.email
    }
    datalist.append(datauser)
    # print(user.name,user.pwd,user.email)
  # print(all_results)
  data['data'] = datalist
  data['success'] = True
  data['message'] = '查询成功'
  return json.dumps(data,ensure_ascii=False)
  return 'user.querall'
@userIndex.route('/user/<username>',methods=['POST','GET'])
def user_user(username):
  # print(request.cookies)
  return render_template('user/user.html',username=username)

@userIndex.route('/user/loginout',methods=['POST','GET'])
def user_loginout():
  response = make_response(redirect(url_for('user_index.user_login'))) # Response("设置cookie")
  response.delete_cookie('username')
  return response
  return redirect(url_for('user_index.user_login'))
@userIndex.route('/user/loginsubmit',methods=['POST','GET'])
def user_loginsubmit():
  username = request.form.get('username')
  password = request.form.get('password')
  result = User.query.filter_by(name=username,pwd=password).all()
  if len(result) > 0:
    response = make_response(redirect(url_for('user_index.user_user',username=username))) # Response("设置cookie")
    expires = datetime.now() + timedelta(days=30,hours=16) 
    # ,expires=expires
    # print(expires)
    response.set_cookie('username',username,domain='0.0.0.0:8989')
    # print(username)
    # print(print(request.cookies.get('username')))
    return response
    # return redirect(url_for('user_index.user_user',username=username))
  else:
    return redirect(url_for('user_index.user_login'))


  # user = User()
  # user.name = username
  # user.pwd=password
  # result = user.queryByNameAndPwd()
  # print(result)
  # return 'afasdfas'
  # redirect('http://localhost:5000/hello')
@userIndex.route('/user/login',methods=['POST','GET'])
def user_login():
  # if request.method=="POST":
    
  # else:
  return render_template('user/login.html')