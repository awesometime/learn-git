https://www.infoq.cn/article/docker-source-code-analysis-part1

   Docker 一个轻量级虚拟化技术容器引擎, 整个项目基于 Go 语言开发。
    
目前，Docker 可以在容器内部快速自动化部署应用，并可以通过内核虚拟

化技术（namespaces 及 cgroups 等）来提供容器的资源隔离与安全保障等。

由于 Docker 通过**操作系统层的虚拟化**实现隔离，所以 Docker 容器在运行时，

不需要类似虚拟机（VM）额外的操作系统开销，提高资源利用率，并且提升诸

如 IO 等方面的性能。

[![docker architecture](https://static001.infoq.cn/resource/image/41/22/41cdc2bdeff20221c67563d673335a22.jpg)](https://static001.infoq.cn/resource/image/41/22/41cdc2bdeff20221c67563d673335a22.jpg)

    Docker 对使用者来讲是一个 C/S 模式的架构，而 Docker 的后端是一个非常
松耦合的架构，模块各司其职，并有机组合，支撑 Docker 的运行。

1) Docker Client
   用户是使用 Docker Client 与 Docker Daemon 建立通信，并发送请求给后者。

2) Docker Daemon   (Docker 架构中的主体部分)
   a) 首先 提供 Server 的功能使其可以接受 Docker Client 的请求；
   b) 而后 Engine 执行 Docker 内部的一系列工作，每一项工作都是以一个 Job 的形式的存在。

3) Driver   (graphdriver networkdriver execdriver)
   Job 的运行过程中，
   a) 当需要容器镜像时，则从 `Docker Registry` 中下载镜像，并通过**镜像管理驱动 graphdriver** 
      将下载镜像以 `Graph` 的形式存储；
   b) 当需要为 Docker 创建网络环境时，通过**网络管理驱动 networkdriver **创建并配置 Docker 
      容器网络环境；
   c) 当需要限制 Docker 容器运行资源或执行用户指令等操作时，则通过** execdriver **来完成。

4) libcontainer (独立的容器管理包)
   networkdriver 以及 execdriver 都是通过 libcontainer 来实现具体对容器进行的操作。

5) Docker container (rootfs layered)
   当执行完运行容器的命令后，一个实际的 Docker 容器就处于运行状态，该容器拥有独立的文件系统，
   独立并且安全的运行环境等。
