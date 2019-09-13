- [libvirt虚拟机xml配置文件详解](http://blog.51cto.com/as007012/1786034)

###  虚拟机相关文件保存位置

libvirt 对CPU的定义提炼出标准的几种类型在 /usr/share/libvirt/cpu_map.xml 可以查到

kvm待启动虚拟机配置模板文件（对cpu disk mem 的定制）位置/etc/libvirt/qemu/                  <---都是xml文件

kvm虚拟机启动后文件保存位置：/var/lib/libvirt/images/                                       <---可以在建立虚拟机时指定    


建立的虚拟机在运行时相关文件及存放位置：

在虚拟机运行时，会在/var/run/libvirt/qemu目录下存放虚拟机的pid文件和配置文件，配置文件与/etc/libvirt/qemu目录下对应的虚拟机文件相同，pid文件保存有此虚拟机进程号。

虚拟机的日志文件存放在/var/log/libvirt/qemu目录下，每个虚拟机一个，文件名称为：虚拟机名称(或UUID)+“.log”


### ubuntu 启动虚拟机方法

1 [使用 virt-manager图形化 启动 KVM 虚机  参考CloudMan](https://mp.weixin.qq.com/s?__biz=MzIwMTM5MjUwMg==&mid=2653587959&idx=1&sn=9bbc07328be70b2cc1a7d3e74563877a&chksm=8d3081eeba4708f8b684ee5d296600085a480b20bbf2e33989def18aa4678346af860c6c8f59&scene=21#wechat_redirect)

2 命令行方法  使用virt-install手动创建qcow2镜像并安装ISO  [参考](https://blog.csdn.net/zhaihaifei/article/details/51153402)
```
命令行创建虚拟机例子

先从http://download.cirros-cloud.net/0.3.3/cirros-0.3.3-x86_64-disk.img下载好cirros-0.3.3-x86_64-disk.img放置在/var/lib/libvirt/images/下

root@cloudlet:/var/lib/libvirt/images# ls
cirros-0.3.3-x86_64-disk.img

root@cloudlet:/var/lib/libvirt/images# qemu-img create -f qcow2 create_for_test.qcow2 10G
Formatting 'create_for_test_81.qcow2', fmt=qcow2 size=10737418240 encryption=off 
cluster_size=65536 lazy_refcounts=off 

root@cloudlet:/var/lib/libvirt/images# ls
cirros-0.3.3-x86_64-disk.img  create_for_test.qcow2

root@cloudlet:/var/lib/libvirt/images# virt-install --virt-type kvm --name create_for_test 
> --ram 1024 --cdrom=/var/lib/libvirt/images/cirros-0.3.3-x86_64-disk.img \
> --disk path=/var/lib/libvirt/images/create_for_test_81.qcow2,format=qcow2 \
> --network network=default \
> --graphics vnc --os-type=linux

Starting install...
Creating domain...                                                                 |    0 B     00:00     
Domain installation still in progress. You can reconnect to 
the console to complete the installation process.

root@cloudlet:/var/lib/libvirt/images# ls
cirros-0.3.3-x86_64-disk.img  create_for_test.qcow2  --disk  --graphics  --network  --ram

root@cloudlet:/var/lib/libvirt/images# virsh list --all
 Id    Name                           State
----------------------------------------------------
 6     create_for_test                running
 
root@cloudlet:/var/lib/libvirt/images# virsh dominfo create_for_test
Id:             6
Name:           create_for_test
UUID:           e98d757c-8fc2-44f4-54c0-38c875fde3fd
OS Type:        hvm
State:          running
CPU(s):         1
CPU time:       69.1s
Max memory:     1048576 KiB
Used memory:    1048576 KiB
Persistent:     yes
Autostart:      disable
Managed save:   no
Security model: none
Security DOI:   0

root@cloudlet:/var/lib/libvirt/images# virsh shutdown create_for_test
Domain create_for_test is being shutdown
root@cloudlet:/var/lib/libvirt/images# virsh list --all              
 Id    Name                           State
----------------------------------------------------
 6     create_for_test                running
root@cloudlet:/var/lib/libvirt/images# virsh destroy create_for_test
Domain create_for_test destroyed
root@cloudlet:/var/lib/libvirt/images# virsh list --all             
 Id    Name                           State
----------------------------------------------------
 -     create_for_test                shut off
root@cloudlet:/var/lib/libvirt/images# virsh start create_for_test 
Domain create_for_test started
root@cloudlet:/var/lib/libvirt/images# virsh list --all            
 Id    Name                           State
----------------------------------------------------
 7     create_for_test                running
root@cloudlet:/var/lib/libvirt/images# virsh
Welcome to virsh, the virtualization interactive terminal.

Type:  'help' for help with commands
       'quit' to quit

virsh # destroy create_for_test  
Domain create_for_test destroyed
virsh # list --all
 Id    Name                           State
----------------------------------------------------
```
3 修改虚拟机模板文件xml启动虚拟机

```sh
#！ /usr/bin/env bash OS='--os-variant=ubuntu16.04' Net='--network model=virtio,bridge=br-int,virtualport_type=openvswitch' Gr='--graphics vnc,listen=0.0.0.0' Cpu='--vcpu=2' Ram='--ram=512' function main() { if [ -z "$1" ];then echo "Uage: ./genVirtOS.h vm-name [vm-mac]" 	exit 1 fi if [ -n "$2" ];then Net="$Net,mac=${2}" fi vName=$1 Net="$Net,target=tap${vName}"w vStorage="/var/lib/libvirt/images/${vName}.img" cp -f ./cirros-0.3.5-x86_64-disk.img "${vStorage}" Name="--name=${vName}" Disk="--disk ${vStorage}" echo $Name $Disk virt-install $OS $Net $Disk $Gr $Cpu $Ram $Name --import --noautoconsole virsh list } main "$@"


sudo apt-get install libxml++2.6-2  libxml++2.6-dev -y
sudo apt-get install libdevmapper-dev -y
sudo apt-get install libpciaccess-dev -y
sudo apt-get install python-dev -y
sudo apt-get install libnl-dev -y


#! /usr/bin/env bash 
function main() { 
if [ "$#" != 1 ];then echo "Uage: ./destroyVirtOS.sh vm-name" exit 1 
fi 
vName="$1" 
virsh destroy ${vName} 
virsh undefine --remove-all-storage ${vName} 
virsh list 
} 

main "$@" 

```
