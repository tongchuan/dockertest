FROM python:3.7-alpine
#MAINTAINET "zhangtch@yonyou.com"
# 虚拟机中的目录
WORKDIR /app

# 设置变量
ENV FLASK_APP run.py
ENV FLASK_RUN_HOST 0.0.0.0
ENV FLASK_ENV development
ENV FLASK_DEBUG TRUE

# COPY ./package.json /app
ADD ./python-web/ /app
RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.ustc.edu.cn/g' /etc/apk/repositories
RUN apk --update --upgrade add mysql-dev\
        build-base 

#RUN apk --update --upgrade add \

#        # bundle 安装相关的依赖
#        git \
#        curl \
#        # mysql2 依赖
#          mysql-dev \
#        # 基础设施，比如gcc相关的东西
#        build-base \
#        # nokogiri 相关依赖
#        libxslt-dev \
#        libxml2-dev \
#        # 图片处理相关依赖
#        imagemagick \
#        # tz相关，如果没有bundle的时候会报错
#        tzdata \
#        nodejs \
#        yarn \
#        && rm -rf /var/cache/apk/*
#libmysqlclient-dev

#RUN pip install virtualenv
#RUN virtualenv --no-site-packages venv
#RUN source venv/bin/activate
RUN pip install flask -i http://mirrors.aliyun.com/pypi/simple/   --trusted-host mirrors.aliyun.com
#RUN pip install flask-mysqldb -i http://mirrors.aliyun.com/pypi/simple/   --trusted-host mirrors.aliyun.com
RUN pip install pymysql -i http://mirrors.aliyun.com/pypi/simple/   --trusted-host mirrors.aliyun.com
RUN pip install flask-sqlalchemy -i http://mirrors.aliyun.com/pypi/simple/   --trusted-host mirrors.aliyun.com
# RUN pip install sqlalchemy -i http://mirrors.aliyun.com/pypi/simple/   --trusted-host mirrors.aliyun.com
RUN pip install -U flask-cors -i http://mirrors.aliyun.com/pypi/simple/   --trusted-host mirrors.aliyun.com
RUN pip install flask-blueprint -i http://mirrors.aliyun.com/pypi/simple/   --trusted-host mirrors.aliyun.com
# RUN pip freeze > requirements.txt
# 安装
#pip install pipreqs
# 在当前目录生成
#pipreqs . --encoding=utf8 --force

#RUN ls
#RUN pip list
#RUN pip install --upgrade pip
#RUN pip list
#RUN mkdir /app/json
#COPY /git.yonyou.com/FC/package.json /app/ 报错 
# copy 是从另一个容器拷贝
#VOLUME ["/git.yonyou.com/docker/python/"] 主机目录无法指定
#RUN ls  #-i http://mirrors.aliyun.com/pypi/simple
#RUN pip install flask==1.1.1
#RUN apt install libmysqlclient-dev
#RUN pip install mysql==0.0.2
#RUN pip install sqlalchemy
#RUN pip install python-mysql
#RUN pip install -U flask-ocrs
#RUN pip install flask-blueprint

#sudo service docker restart 


# 暴露端口
EXPOSE 5000 

CMD ["flask", "run"]


# docker build -t python:flask .
# 查看结果：
# docker image ls
# docker rmi python:flask
# sudo docker run -p 5000:5000 --name python --network testnet -v /git.yonyou.com/docker/python/python-web:/app -d python:flask
# docker run -p 5000:5000 --name python -v /git.yonyou.com/docker/python/python-web:/app -d python:flask --link mysql
#sudo docker inspect mysql
# 镜像名 pythonhello 后面，什么都不用写，因为在 Dockerfile 中已经指定了 CMD。否则，就得把进程的启动命令加在后面：
# -p 外网：内网
# docker run -p 80:5000 pythonhello
# 查看容器 
# docker ps
# 删除容器docker rm 083084e11bc5
# 进入容器：
# docker exec -it pythonhello /bin/bash
# 访问容器内应用：
# curl http://localhost:4000
#docker stop <容器 ID>
#docker restart <容器 ID>

# docker stop python
# docker start python
# docker restart python
# docker system df
