
-[深度实践 OpenStack   基于Python的OpenStack组件开发 - 喻涛 机械工业出版社](https://read.douban.com/reader/ebook/49007537/)

-[阅读 openstack 源码](http://www.cnblogs.com/liujiacai/p/9232316.html)

#### install 
```
由于国外资源下载问题，并且已经有一个机子已经下载成功。
因为 elijah 通过脚本 pip 下载的文件都被安装于位置 /usr/local/lib/python2.7/dist-packages/下，
所以将成功了的机子上的/usr/local/lib/python2.7/dist-packages/中的文件复制到 windows，再复制到需要安装elijah 的 2.60机子上。
搞定。

为备以后用，已将dist-packages包备份到百度云，使用时将dist-packages 1234合到一起，合成一个文件夹，放到/usr/local/lib/python2.7/下
```
#### 源码分析之setup.cfg文件

- [Read-only mirrors of a mix of official and unofficial projects hosted at https://git.openstack.org/cgit/openstack/ by the OpenStack community.](https://github.com/openstack)
```
OpenStack所有项目都是基于Python开发，都是标准的Python项目，通过setuptools工具管理项目，负责Python包的安装和分发。
想知道一个项目有哪些服务组成，入口函数（main函数）在哪里，最直接的方式就是查看项目根目录下的setup.cfg文件。


例如找到[openstack nova源码](https://github.com/openstack/nova)，其中setup.py如下
>>>
>>>
>>>openstack/nova/setup.py
import setuptools

# In python < 2.7.4, a lazy loading of package `pbr` will break
# setuptools if some other modules registered functions in `atexit`.
# solution from: http://bugs.python.org/issue15881#msg170215
try:
    import multiprocessing  # noqa
except ImportError:
    pass

setuptools.setup(
    setup_requires=['pbr>=2.0.0'],
    pbr=True)

>>>
>>>
>>>openstack/nova/setup.cfg          # 详见具体网址

[entry_points]
oslo.config.opts =
    nova.conf = nova.conf.opts:list_opts

oslo.config.opts.defaults =
    nova.conf = nova.common.config:set_middleware_defaults

oslo.policy.enforcer =
    nova = nova.policy:get_enforcer
    placement = nova.api.openstack.placement.policy:get_enforcer

oslo.policy.policies =
    # The sample policies will be ordered by entry point and then by list
    # returned from that entry point. If more control is desired split out each
    # list_rules method into a separate entry point rather than using the
    # aggregate method.
    nova = nova.policies:list_rules
    placement = nova.api.openstack.placement.policies:list_rules

nova.compute.monitors.cpu =
    virt_driver = nova.compute.monitors.cpu.virt_driver:Monitor

console_scripts =                                         # console_scripts就是所有服务组件的入口
    nova-api = nova.cmd.api:main
    nova-api-metadata = nova.cmd.api_metadata:main
    nova-api-os-compute = nova.cmd.api_os_compute:main
    nova-cells = nova.cmd.cells:main
    nova-compute = nova.cmd.compute:main
    nova-conductor = nova.cmd.conductor:main
    nova-console = nova.cmd.console:main
    nova-consoleauth = nova.cmd.consoleauth:main
    nova-dhcpbridge = nova.cmd.dhcpbridge:main
    nova-manage = nova.cmd.manage:main
    nova-network = nova.cmd.network:main
    nova-novncproxy = nova.cmd.novncproxy:main
    nova-policy = nova.cmd.policy:main
    nova-rootwrap = oslo_rootwrap.cmd:main
    nova-rootwrap-daemon = oslo_rootwrap.cmd:daemon
    nova-scheduler = nova.cmd.scheduler:main
    nova-serialproxy = nova.cmd.serialproxy:main
    nova-spicehtml5proxy = nova.cmd.spicehtml5proxy:main
    nova-status = nova.cmd.status:main
    nova-xvpvncproxy = nova.cmd.xvpvncproxy:main
wsgi_scripts =
    nova-placement-api = nova.api.openstack.placement.wsgi:init_application
    nova-api-wsgi = nova.api.openstack.compute.wsgi:init_application
    nova-metadata-wsgi = nova.api.metadata.wsgi:init_application

nova.ipv6_backend =
    rfc2462 = nova.ipv6.rfc2462
    account_identifier = nova.ipv6.account_identifier

nova.scheduler.driver =
    filter_scheduler = nova.scheduler.filter_scheduler:FilterScheduler
    caching_scheduler = nova.scheduler.caching_scheduler:CachingScheduler
    fake_scheduler = nova.tests.unit.scheduler.fakes:FakeScheduler


```
#### openstack 源代码经过 编译后的文件的位置
```
1 horizon
Horizon项目核心的代码包有两个：openstack-dashboard和python-django-horizon。
第一个包是控制台代码的具体实现，是一个基于Django框架的web应用，安装后主要文件在:路径下。
第二个包是通用的一些Python类库，也包括一些静态文件，安装后在/usr/lib/python2.7/dist-packages/horizon/下。
定制化开发，主要是修改业务代码，基本不需要修改python-django-horizon，所以我们分析的重点放在openstack-dashboard这个包上。

2 nova

nova-api
/usr/lib/python2.7/dist-packages/nova/api/openstack/compute/servers
/usr/lib/python2.7/dist-packages/nova/api/openstack/wsgi.py

nova/cert
nova/conductor
nova/consoleauth
nova/dhcpbridge
nova/manager.py
nova-network
nova-novncproxy

nova-compute
/usr/lib/python2.7/dist-packages/nova/compute/api.py
/usr/lib/python2.7/dist-packages/nova/compute/manager.py

nova-virt
/usr/lib/python2.7/dist-packages/nova/virt/libvirt.*

nova-scheduler
/usr/lib/python2.7/dist-packages/nova/scheduler.*

3 glance
/usr/lib/python2.7/dist-packages/glance/api/v1/images.py
/usr/lib/python2.7/dist-packages/glance/
/usr/lib/python2.7/dist-packages/glance/
/usr/lib/python2.7/dist-packages/glance/

4 neutron




```
- [glance v1 源码解析](https://blog.csdn.net/S1234567_89/article/details/52595547)



#### 配置文件位置
    
    vim /etc/nova/nova.conf

#### 日志文件位置
    
    vim /var/log/nova


```
# grep -r l3driver *
# **grep -r req-e0abe769-6706-4258-89ac-941363b833de ***
# nova floating-ip-associate <server> <ip>
# nova floating-ip-associate e9dccc8d-bf7c-45a6-86a7-c6ed77ab8f81 192.168.71.153
# grep -rn "connectCompareCPU" ./src/
# tail -f
# ps -aux |grep glance
# awk “样式” 文件： 把符合样式的数据行显示出来。
# cat  /proc/cpuinfo | grep vmx --color
# cat  /proc/meminfo
## KVM关于CPU型号的定义
   libvirt 对CPU的定义提炼出标准的几种类型在 /usr/share/libvirt/cpu_map.xml 可以查到
##
cloudlet command  [option] -- [qemu-options]
  EX) cloudlet.py base /path/to/disk.img

Command list:
  info-overlay         : show information of the VM overlay
  import-base          : import base VM from a exported file
  base                 : create new base VM
  list-base            : show all base VM at this machine
  synthesis            : test created overlay using command line
  overlay              : create new overlay VM on top of base VM
  list-session         : list all the session history
  add-base             : add existing base vm to DB
  del-base             : delete base vm at database
  list-overlay         : list all the overlay history
  export-base          : export base VM into a portable file
#####
# cat /proc/cpuinfo |grep flags
# virsh
Welcome to virsh, the virtualization interactive terminal.
# virsh dumpxml instance号
# kvm --version
```



```
命令行command


openstack server show id号

nova list                  虚拟机创建好以后查看虚拟机状态
nova show id号
nova network-list
nova network-show id号
nova network-delete id号
nova floating-ip-list
nova service-list
nova-manage service list
nova image-show id号或image名

nova floating-ip-associate       Associate a floating IP address to a server.
nova floating-ip-bulk-create     Bulk create floating IPs by range.
     floating-ip-bulk-delete     Bulk delete floating IPs by range.
     floating-ip-bulk-list       List all floating IPs.
     floating-ip-create          Allocate a floating IP for the current tenant.
     floating-ip-delete          De-allocate a floating IP.
     floating-ip-disassociate    Disassociate a floating IP address from a server.
     floating-ip-list            List floating IPs.
     floating-ip-pool-list       List all floating IP pools.

service nova-compute status
service nova-compute start

glance image-list
glance image-show id号

cloudlet list-base
cloudlet overlay [path to base VM]

ssh root@ip
ssh 普通用户@ip             没试过，估计不能

```


#### 通过demo学习OpenStack开发所需的基础知识 -- 软件包管理
- [通过demo学习OpenStack开发所需的基础知识 -- 软件包管理](https://segmentfault.com/a/1190000002940724)
这部分扯远了，开发！！！
