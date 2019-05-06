### 
```
docker version
docker info
docker run --cap-add dac_read_search --name lxlxlx -it 100.125.5.235:20202/huyue/nginx:latest /bin/sh
docker images
docker ps|grep nginx|awk '{print $1}'
docker exec
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
