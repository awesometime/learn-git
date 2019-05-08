参考 [CentOS7下部署Django项目详细操作步骤](https://www.django.cn/article/show-4.html#banqian)

[架构图片有助理解](https://www.bilibili.com/video/av10244432/?spm_id_from=333.788.videocard.0)

【浏览】  http协议   【Nginx】  socket协议   【uwsgi】   wsgi协议   【Django】

【uwsgi】   wsgi协议   【Django】 这部分放在虚拟环境

### 注意

    【uwsgi要安装两次，先在系统里安装一次，然后进入对应的虚拟环境安装一次】
    [root@nodelete-djg-docker-master-3vmqs ~]#       # 外边系统装好uwsgi
    [root@nodelete-djg-docker-master-3vmqs ~]# cd /usr/local/env/django-env/bin                      
    [root@nodelete-djg-docker-master-3vmqs bin]# . activate
    (django-env) [root@nodelete-djg-docker-master-3vmqs bin]# cd /usr/local/djg-docker/Mxonline3/   
    (django-env) [root@nodelete-djg-docker-master-3vmqs Mxonline3]# uwsgi -x Mxonline3.xml    # 启动 虚拟环境的 uwsgi
    [uWSGI] parsing config file Mxonline3.xml

    # 启动nginx
    cd /usr/local/nginx/sbin
    ./nginx

    ps aux|grep nginx
    ps aux|grep uwsgi

    netstat -apn|grep nginx
    netstat -apn|grep 80


    killall -9 nginx
    killall -9 uwsgi

    wget http://127.0.0.1:80
    curl http://127.0.0.1:80
    curl http://127.0.0.1:80/org/list

### uwsgi

命令行启动
uwsgi --http :8009 --module /usr/local/djg-docker/Mxonline3/Mxonline3.wsgi

uwsgi   xml   ini
uwsgi -x Mxonline3.xml 启动
```xml
<!-- Mxonline3.xml --> 
<uwsgi>    
   <socket>127.0.0.1:8997</socket> <!-- 内部端口，自定义 --> 
   <chdir>/usr/local/djg-docker/Mxonline3/</chdir> <!-- 项目路径 -->            
   <module>Mxonline3.wsgi</module>  <!-- mysite为wsgi.py所在目录名--> 
   <processes>4</processes> <!-- 进程数 -->     
   <daemonize>uwsgi.log</daemonize> <!-- 日志文件 -->
</uwsgi>
```

### nginx

nginx.conf
```conf
events {
    worker_connections  1024;
}
http { 
    include       mime.types;
    default_type  application/octet-stream;
    sendfile        on;
    server {
        listen 80;
        server_name  127.0.0.1:80;                                            #改为自己的域名，没域名修改为127.0.0.1:80
        charset utf-8;
        location / {
           include uwsgi_params;
           uwsgi_pass 127.0.0.1:8997;                                          #端口要和uwsgi里配置的一样
           uwsgi_param UWSGI_SCRIPT Mxonline3.wsgi;                            #wsgi.py所在的目录名+.wsgi
           uwsgi_param UWSGI_CHDIR /usr/local/djg-docker/Mxonline3/;           #项目路径
           
        }
        location /static/ {
        alias /usr/local/djg-docker/Mxonline3/static/;                         #静态资源路径
        }
    }
}
```
