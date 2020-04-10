FROM nginx:1.17.9

MAINTAINER zhangtch@yonyou.com

WORKDIR /usr/share/nginx/html

RUN chmod -R 777 /usr/share/nginx/html
RUN chmod -R 777 /var/log/nginx/
RUN chmod -R 777 /etc/nginx/conf.d/

EXPOSE 80
#CMD ["nginx","-g","daemon off;"]



#nginx version: nginx/1.17.9

#/etc/nginx#
#/etc/nginx/conf.d
#/var/log/nginx/host.access.log
#/usr/share/nginx/html

# docker run -it -p 80:80  -v `pwd`/logs:/var/log/nginx dockerfile/nginx

#/git.yonyou.com/docker/nginx




#docker build -t nginx:html .
# docker run -p 80:80 --name nginx --network testnet -v /git.yonyou.com/docker/nginx/html:/usr/share/nginx/html -v /git.yonyou.com/docker/nginx/log/:/var/log/nginx/ -v /git.yonyou.com/docker/nginx/conf/default.conf:/etc/nginx/conf.d/default.conf -v /git.yonyou.com/docker/nginx/conf/nginx.conf:/etc/nginx/nginx.conf -d nginx:html
# docker stop nginx
# docker start nginx
