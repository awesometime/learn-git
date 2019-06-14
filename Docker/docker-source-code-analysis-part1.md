https://www.infoq.cn/article/docker-source-code-analysis-part1

Docker 一个轻量级虚拟化技术容器引擎, 整个项目基于 Go 语言开发。
    
目前，Docker 可以在容器内部快速自动化部署应用，并可以通过内核虚拟

化技术（namespaces 及 cgroups 等）来提供容器的资源隔离与安全保障等。

由于 Docker 通过**操作系统层的虚拟化**实现隔离，所以 Docker 容器在运行时，

不需要类似虚拟机（VM）额外的操作系统开销，提高资源利用率，并且提升诸

如 IO 等方面的性能。

[![docker architecture](https://static001.infoq.cn/resource/image/41/22/41cdc2bdeff20221c67563d673335a22.jpg)](https://static001.infoq.cn/resource/image/41/22/41cdc2bdeff20221c67563d673335a22.jpg)

Docker 对使用者来讲是一个 C/S 模式的架构，而 Docker 的后端是一个非常松耦合的架构，模块各司其职，并有机组合，支撑 Docker 的运行。

Docker的设计是单机的，不是分布式的

1) **Docker Client**
   
   用户是使用 Docker Client 与 Docker Daemon 建立通信，并发送请求给后者。三种方式和Docker Daemon建立通信：
   
   tcp://host:port
   
   unix://path_to_socket
   
   fd://socketfd

2) **Docker Daemon**   (Docker 架构中的主体部分 Server Engine Job)
   
   a) 首先 提供 `Server` 的功能使其可以接受 Docker Client 的请求；
   
   b) 而后 `Engine` 执行 Docker 内部的一系列工作，每一项工作都是以一个 `Job` 的形式的存在。

3) **Driver**   (graphdriver networkdriver execdriver)
  
   `Job` 的运行过程中，
   
   a) 当需要容器镜像时，则从 `Docker Registry` 中下载镜像，并通过**镜像管理驱动 graphdriver** 将下载镜像以 `Graph` 的形式存储；
   
   b) 当需要为 Docker 创建网络环境时，通过**网络管理驱动 networkdriver**创建并配置 Docker 容器网络环境；
   
   c) 当需要限制 Docker 容器运行资源或执行用户指令等操作时，则通过 **容器执行驱动 execdriver** 来完成。

4) **libcontainer** (独立的容器管理包)
   
   networkdriver 以及 execdriver 都是通过 libcontainer 来实现具体对容器进行的操作。

5) **Docker container** (rootfs layered)
   
   当执行完运行容器的命令后，一个实际的 Docker 容器就处于运行状态，该容器拥有独立的文件系统，独立并且安全的运行环境等。


### 目录结构

```
.
├── api
├── builder
├── cli
├── client
├── cmd  # 命令行的入口，我们就要从这里跳进去看
├── container  # 容器的抽象
├── contrib  # 杂物堆，啥杂七杂八的都往这里丢
├── daemon  # 今天的主角，dockerd这个daemon
├── distribution  # 看起来发布相关的
├── dockerversion
├── docs  # 文档
├── errdefs  # 一些常见的错误
├── hack
├── image  # 镜像的抽象概念
├── integration
├── integration-cli
├── internal
├── layer  # 层。怎么说呢，就是对各种layer fs的抽象
├── libcontainerd
├── migrate
├── oci  # https://blog.docker.com/2017/07/demystifying-open-container-initiative-oci-specifications/ 容器标准库相关
├── opts  # 一些配置和配置校验相关的
├── pkg  # 类似于我们平时写的utils或者helpers等
├── plugin  # 插件相关的东西
├── profiles
├── project
├── reference
├── registry
├── reports
├── restartmanager  # 负责容器的重启，比如是否设置了"always"呀
├── runconfig
├── vendor  # go的vendor机制
└── volume  # volume相关
```


### 启动 server 和 daemon

    从命令行进入
    入口在  `cmd/dockerd/docker.go`
    跳到 `cmd/dockerd/daemon.go` 加载配置,设置相关的变量和配置,监听端口,设置信号handler,启动起了API server,等待接受请求,启动 服务端 daemon.


### 创建容器

    以命令行输入docker run 为例
    daemon启动完之后就**等待请求**了。我们要找一个新的入口点去跟踪 代码，所以我选择 docker run。从 docker/cli 库翻了翻，发现最后是调用 containers/create 这样一个接口。然后就在本仓库里搜索，我们的目标是找到处理这个请求的mux **路由**所在地，然后翻出对应的 handler api/server/router/container/container.go，然后跳到 api/server/router/container/container_routes.go:
    daemon/create.go
    daemon/container.go
