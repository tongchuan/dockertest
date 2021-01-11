FROM centos:latest

MAINTAINER tongchuanxing@163.com

ENV R_DIR /usr/local/redis
ENV I_DIR /opt/redis-6.0.9


ADD redis-6.0.9.tar.gz /usr/local
RUN mv /usr/local/redis-6.0.9 $R_DIR
# RUN yum -y upgrade
RUN yum -y install gcc gcc-c++ make
RUN cd $R_DIR \
  && make \
  && sed -i 's/\# requirepass foobared/requirepass 123456/g' $R_DIR/redis.conf

#    && cd src/ \
#    && make install PREFIX=/usr/local/redis
#RUN mkdir -p /usr/local/redis && \
#    cp $I_DIR/redis.conf $R_DIR/ && \
#    cp $I_DIR/sentinel.conf $R_DIR/ && \
#    cp $I_DIR/src/redis-benchmark $R_DIR && \
#    cp $I_DIR/src/redis-check-aof $R_DIR && \
#    cp $I_DIR/src/redis-check-dump $R_DIR && \
#    cp $I_DIR/src/redis-cli $R_DIR && \
#    cp $I_DIR/src/redis-sentinel $R_DIR && \
#    cp $I_DIR/src/redis-server $R_DIR && \
#    sed -i 's/\# bind 127\.0\.0\.1/bind 0\.0\.0\.0/g' $R_DIR/redis.conf && \
#    sed -i 's/\# requirepass foobared/requirepass 123456/g' $R_DIR/redis.conf


VOLUME ["/usr/local/redis"]

EXPOSE 6379


CMD ["/usr/local/redis/src/redis-server","/usr/local/redis/redis.conf"]





# logfile ""
# dbfilename dump.rdb

# docker build -t centos:redis .
# docker run -p 6379:6379 --name redis -v /git.yonyou.com/docker/redis/redis.conf:/usr/local/redis/redis.conf -d centos:redis --network=mynet --ip 172.18.12.1 

# docker run -p 6379:6379 --name redis -v /git.yonyou.com/docker/redis/redis.conf:/usr/local/redis/redis.conf -d centos:redis --net bridge --ip 192.168.0.2
# docker exec -it redis bash
# docker start redis 
# docker stop redis 
# ./redis-cli
# auth "yourpassword"
# ping
# SELECT index
# flushdb命令清除数据，

# sudo docker network ls
# 创建自定义网络类型，并且指定网段
# sudo docker network create --subnet=192.168.0.0/16 staticnet

# docker inspect redis 查看IP


# docker build -t redis:ztc .
# docker run -p 6379:6379 --name redis -d redis:ztc
# docker exec -it redis bash


# sudo docker ps -a
# docker rm 容器id
# docker rmi 镜像id
# sudo docker stop redis
# sudo docker images
# sudo docker search redis


# 查看网络模式
# docker network ls 

# 创建一个新的bridge网络
# docker network create --driver bridge --subnet=172.18.12.0/16 --gateway=172.18.1.1 mynet

# 查看网络信息
# docker network inspect mynet

# 创建容器并指定容器ip
# docker run -e TZ="Asia/Shanghai" --privileged -itd -h hadoop01.com --name hadoop01 --network=mynet --ip 172.18.12.1 centos /usr/sbin/init