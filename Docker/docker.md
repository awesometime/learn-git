### 
```
docker ps|grep nginx|awk '{print $1}'

service docker restart
docker info
docker version
docker search image_name
docker list
docker login -u usename -p password ip:port
docker run --privileged=true -d -v /etc/localtime:/etc/localtime:ro -v /var/log:/usr/local/shield/log  --net=host --pid=host --cap-add=NET_ADMIN  --cap-add=SYS_ADMIN  --cap-add=SYS_PTRACE  --cap-add AUDIT_CONTROL  --cpu-period=100000 --cpu-quota=20000 --restart=always --env CSS_MASTER_ADDR="https://xxxxxxxxx100.31.33.243:443/ho/websocket" 10.15.8.12:20202/test/cty:1.0.0
docker container start
docker container stop
docker save -o /root/cgs-shield-1.0.9.tar 100.95.181.176:5300/op_svc_cgs_container0/cgs-shield:1.0.9
docker load -i cgs-shield-1.0.9.tar 
docker pull 100.95.181.176:5300/op_svc_cgs_container0/cgs-shield:1.0.9
docker push
docker exec -it docker_id /bin/sh          登录进入容器
docker exec -it xxx pip install flask -i http://mirrors.tools.huawei.com/pypi/simple/ --trusted-host mirrors.tools.huawei.com
docker attach 
docker build
docker images
docker rmi                                 删除镜像
docker ps
docker stop docker_id                      停止容器
docker rm docker_id                        删除停止的docker
docker rm -f docker_id                     删除运行的docker
docker container prune
docker start  ea508b1c2440 /bin/sh
docker inspect 62ba
docker cp file_name docker_id:目录         在节点使用命令上传文件到容器
```

```shell
[root@test-fjm-nodelete-32994-47hy0 ~]# ls
ContainerShieldInstall.sh  shocker  shocker.tgz  test  wget.log
[root@test-fjm-nodelete-32994-47hy0 ~]# docker images
REPOSITORY                                                  TAG                 IMAGE ID            CREATED             SIZE
100.125.5.235:20202/op_svc_apm/icagent                      5.11.1              a1ab7b170e87        9 days ago          342MB
100.125.5.235:20202/hwofficial/storage-driver-linux-amd64   1.0.9               a5c1b58fc431        2 weeks ago         752MB
canal-agent                                                 1.0.RC8.B060        7dc1d1a3b40c        2 months ago        505MB
canal-agent                                                 latest              7dc1d1a3b40c        2 months ago        505MB
cgs-shield                                                  1.0.0               f99f936550ec        5 months ago        397MB
100.125.5.235:20202/huyue/tomcat                            latest              2d43521f2b1a        8 months ago        462MB
100.125.5.235:20202/huyue/nginx                             latest              ae513a47849c        10 months ago       109MB
euleros                                                     2.2.5               b0f6bcd0a2a0        16 months ago       289MB
100.125.5.235:20202/h00425574/tomcat                        latest              ee30af84161d        19 months ago       439MB
100.125.5.235:20202/huyue/busy-job                          latest              741f24a795d6        2 years ago         1.09MB
100.125.5.235:20202/h00425574/nginx                         latest              d04d812f5048        2 years ago         183MB
100.125.5.235:20202/huyue/busybox                           latest              3d89db42c4d1        2 years ago         4.18MB
100.125.5.235:20202/huyue/resource_consumer                 latest              18e4d10ad776        3 years ago         133MB
cfe-pause                                                   11.20.1             2b58359142b0        3 years ago         350kB

# 启动一个挂载了/root:/root目录的容器  前一个/root指宿主的目录 后一个/root指容器的目录
# 这样新建进入容器的/root目录  ls 显示的就是宿主/root的内容
[root@test-fjm-nodelete-32994-47hy0 ~]# docker run -v /root:/root/ -it 100.125.5.235:20202/huyue/busybox:latest /bin/sh
/ # cd root
~ # ls
ContainerShieldInstall.sh  shocker                    shocker.tgz                test                       wget.log
~ # touch ttest
~ # ls
ContainerShieldInstall.sh  shocker                    shocker.tgz                test                       ttest                      wget.log
~ # touch wget.log
~ # ls
ContainerShieldInstall.sh  shocker                    shocker.tgz                test                       ttest                      wget.log
~ #
```
