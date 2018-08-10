
[深度实践OpenStack   基于Python的OpenStack组件开发 - 喻涛 机械工业出版社](https://read.douban.com/reader/ebook/49007537/)
```
# grep -r l3driver *
# **grep -r req-e0abe769-6706-4258-89ac-941363b833de ***
# nova floating-ip-associate <server> <ip>
# nova floating-ip-associate e9dccc8d-bf7c-45a6-86a7-c6ed77ab8f81 192.168.71.153
# grep -rn "connectCompareCPU" ./src/
# tail -f
# cat  /proc/cpuinfo | grep vmx --color
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
vim /etc/nova/nova.conf


nova list  虚拟机创建好以后查看虚拟机状态
nova show id号
nova network-list
nova network-show id号
nova network-delete id号
nova floating-ip-list
nova service-list
nova-manage service list
nova image-show id号或image名
nova floating-ip-bulk-create
nova floating-ip-bulk-delete
service nova-compute status
service nova-compute start
cloudlet list-base
cloudlet overlay [path to base VM]


```
