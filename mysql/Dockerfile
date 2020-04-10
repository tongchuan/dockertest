FROM mysql:5.7

MAINTAINER zhangtch@yonyou.com

WORKDIR /etc/mysql/


RUN chmod -R 777 /etc/mysql/
RUN chmod -R 777 /var/log/mysql/
RUN chmod -R 777 /var/lib/mysql

#WORKDIR /mysql_data
#ENV MYSQL_ROOT_PASSWORD root
#RUN echo $PWD \
#  ls -al

EXPOSE 3306

# docker build -t mysql:ztc .
# docker run -p 3306:3306 --name mysql -e MYSQL_ROOT_PASSWORD=root -v /git.yonyou.com/docker/mysql/conf/my.conf:/etc/mysql/my.conf -v /git.yonyou.com/docker/mysql/logs/:/var/log/mysql/ -v /git.yonyou.com/docker/mysql/data:/mysql_data -d mysql:ztc 






## docker stop mysql
## docker start mysql
# docker network create -d bridge testnet

# docker build -t mysql:data .
#docker run -p 3306:3306 --name mysql --network testnet -e MYSQL_ROOT_PASSWORD=root -v /git.yonyou.com/docker/mysql/conf/:/etc/mysql/ -v /git.yonyou.com/docker/mysql/logs/:/var/log/mysql/ -v /git.yonyou.com/docker/mysql/data:/var/lib/mysql -d mysql:data
# docker exec -it mysql bash
# mysql -u root -p
#GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' IDENTIFIED BY 'root' WITH GRANT OPTION;
#FLUSH PRIVILEGES;

# 127.0.0.1
# root
# root
# mysql