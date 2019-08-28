### 官方

[docs.docker.com ](https://docs.docker.com/get-started/)

[dockone.io](http://dockone.io/)

### 学习

[Docker —— 从入门到实践  gitbook](https://yeasy.gitbooks.io/docker_practice/)

[几张图帮你理解 docker 基本原理及快速入门](https://www.cnblogs.com/SzeCheng/p/6822905.html)

[阮一峰的日志  Docker 入门教程](http://www.ruanyifeng.com/blog/2018/02/docker-tutorial.html)

[图片帮助理解](https://github.com/CyC2018/CS-Notes/blob/master/notes/Docker.md)

[利用思维导图整理的docker知识点](https://github.com/Weiwf/docker-mindmap)

### 源码分析

infoQ  

深入浅出Docker  

Docker源码分析

[Docker源码分析](https://s.geekbang.org/search/c=0/k=docker%20%E6%BA%90%E7%A0%81%E5%88%86%E6%9E%90/t=)


### 安装

[windows下安装docker](https://blog.csdn.net/tina_ttl/article/details/51372604)

[阿里云  windows/docker-toolbox 镜像](http://mirrors.aliyun.com/docker-toolbox/windows/docker-toolbox/)

[daocloud  windows/docker-toolbox 镜像](https://get.daocloud.io/toolbox/)

### 使用镜像

[daocloud 镜像市场](https://hub.daocloud.io/)

### 面试

[这可能是最为详细的Docker入门吐血总结](https://www.cnblogs.com/ECJTUACM-873284962/p/9789130.html)

```
优势
基本概念
架构
组件协作 client daemon
常用命令
Dockerfile
容器与镜像的关系类似于面向对象编程中的对象与类
```
[dockone.io  cgroup, namespace和unionFS](http://dockone.io/article/2941)

[Docker技术三大要点：cgroup, namespace和unionFS的理解](https://yq.aliyun.com/articles/680943#)

[cgroups](https://www.infoq.cn/article/docker-kernel-knowledge-cgroups-resource-isolation/)

[进阶再看:  coolshell   DOCKER基础技术 ](https://coolshell.cn/?s=DOCKER%E5%9F%BA%E7%A1%80%E6%8A%80%E6%9C%AF)
```
cgroup   图片 https://www.infoq.cn/article/docker-kernel-knowledge-cgroups-resource-isolation/
namespace
unionFS   DEVICEMAPPER  AUFS overlay2
```
[言简意赅讲解 Cgroup和Namespace](https://blog.csdn.net/xiangxianghehe/article/details/70569920)

[Linux Namespace和Cgroup 详解](https://segmentfault.com/a/1190000009732550)

```
1 CGroups 资源分配
Control Groups（简称 CGroups）就是能够隔离宿主机器上的物理资源，例如 CPU、内存、磁盘 I/O 和网络带宽

四个概念      task（任务）cgroup（控制组）subsystem（子系统）hierarchy（层级树）

hierarchy（层级树）
  |
  ---cgroup 1  一组进程
  ---cgroup 2
  
一个 hierarchy 关联一个或多个 subsystem 指定一些规则，比如
CPU 子系统可以控制 CPU 时间分配，
内存子系统可以限制 cgroup 内存使用量

task（任务）== 一个进程


2 Namespaces 权限隔离

CLONE_NEWIPC
CLONE_NEWNET
CLONE_NEWNS
CLONE_NEWPID
CLONE_NEWUSER 
CLONE_NEWUTS

2.1 讲讲网络namespace
2.1.1 Namespaces-CLONE_NEWNET 
同一主机容器间通信??  不同主机容器间通信??

Docker 为我们提供了四种不同的网络模式，Host、Container、None 和 Bridge 模式。默认的网络设置模式：网桥模式
在这种模式下，Docker 服务端做哪些工作
分配隔离的网络命名空间
为所有的容器设置 IP 地址。
创建新的虚拟网桥 docker0，docker run起的容器默认情况下都与该网桥docker0相连。
创建一对虚拟网卡，两个虚拟网卡组成了数据的通道，其中一个会放在创建的容器中，会加入到名为 docker0 网桥中。
通过 iptables 进行数据包转发

Docker 通过 Linux 的命名空间实现了网络的隔离，又通过 iptables 进行数据包转发，让 Docker 容器能够优雅地为
宿主机器或者其他容器提供服务。

Docker 创建一个容器的时候，会执行如下操作：

创建一对虚拟接口，分别放到本地主机和新容器中；
本地主机一端桥接到默认的 docker0 或指定网桥上，并具有一个唯一的名字，如 veth65f9；
容器一端放到新容器中，并修改名字作为 eth0，这个接口只在容器的名字空间可见；
从网桥可用地址段中获取一个空闲地址分配给容器的 eth0，并配置默认路由到桥接网卡 veth65f9。
完成这些之后，容器就可以使用 eth0 虚拟网卡来连接其他容器和其他网络。

2.1.2 Libnetwork
具体实现 通过Libnetwork 
整个网络部分的功能都是通过 Docker 拆分出来的 libnetwork 实现的，它提供了一个连接不同容器的实现，同时也能够
为应用给出一个能够提供一致的编程接口和网络层抽象的容器网络模型。

在容器网络模型中，三个概念
Sandbox
存储着当前容器的网络栈配置，包括容器的接口、路由表和 DNS 设置，Linux 使用网络命名空间实现这个 Sandbox
Endpoint
每一个 Sandbox 中都可能会有一个或多个 Endpoint，在 Linux 上就是一个虚拟的网卡 veth
Network
Sandbox 通过 Endpoint 加入到对应的网络中，这里的网络可能就是我们在上面提到的 Linux 网桥bridge或者 VLAN

3 UnionFS ——镜像分层提高存储效率
Docker 中的每一个镜像都是由一系列只读的层组成的，Dockerfile 中的每一个命令都会在已有的只读层上创建一个新的层。
当镜像被 docker run 命令创建时就会在镜像的最上层添加一个可写的层，也就是容器层，所有对于运行时容器的修改其实
都是对这个容器读写层的修改。容器和镜像的区别就在于，所有的镜像都是只读的，而每一个容器其实等于镜像加上一个
可读写的层，也就是同一个镜像可以对应多个容器。

3.1 存储驱动
aufs、devicemapper、overlay2、zfs 和 vfs 等等，在最新的 Docker 中，overlay2 取代了 aufs 成为了推荐的存储驱动，
但是在没有 overlay2 驱动的机器上仍然会使用 aufs 作为 Docker 的默认驱动。

3.1.1 AUFS
Advanced UnionFS 其实就是 UnionFS 的升级版
/var/lib/docker/ 目录
/var/lib/docker/aufs/diff/ 目录中存储所有镜像层和容器层的内容
/var/lib/docker/aufs/layers/ 中存储着镜像层的元数据，每一个文件都保存着镜像层的元数据
/var/lib/docker/aufs/mnt/ 包含镜像或者容器层的挂载点
最终会被 Docker 通过联合的方式进行组装。
```

[同宿主机容器和不同宿主机容器之间怎么通信](https://blog.51cto.com/2367685/2349762)
