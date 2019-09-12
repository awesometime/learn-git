```
https://cloud.tencent.com/developer/article/1082724
https://www.sdnlab.com/19532.html
https://segmentfault.com/a/1190000019612525#articleHeader17
https://xiexianbin.cn/openvswitch/2015-05-23-openvswitch-complete-manual/#20OpenFlowTrace
```

#### 

```
ovs-vsctl show    查看网桥
ovs-vsctl list interface interface_name  查看interface
ovs-vsctl -- --columns=name,ofport list Interface
```
```
ovs-vsctl show
21e4d4c5-cadd-4dac-b025-c20b8108ad09
    Bridge "ovs0"
        Port "f1c0a9d0994d4_l"
            tag: 100
            Interface "f1c0a9d0994d4_l"
        Port "121c6b2f221c4_l"
            tag: 100
            Interface "121c6b2f221c4_l"
```

#### 流表相关 ovs-ofctl OpenFlow

priority数值越大，优先级越高
```
ovs-ofctl dump-flows brA   查看流表信息
ovs-ofctl del-flows brA    删除流表
ovs-ofctl show brA         查看端口信息
配置流表
ovs-ofctl add-flow brA "ip,nw_dst=ip地址 actions=mod_dl_dst:mac地址,output:3"
ovs-ofctl add-flow brA "priority=1,in_port=3,actions=output:4"  同网段
配置arp流表项 处理ARP请求
ovs-ofctl add-flow brA "priority=100,arp,arp_tpa=ip地址 actions=output:3"
ovs-ofctl add-flow brA "table=0,priority=65535,arp,arp_tpa=10.0.0.254 actions=LOCAL"
ovs-ofctl add-flow brA "priority=65535,arp,arp_tpa=ip地址 actions=NORMAL"
ovs-ofctl add-flow brA "priority=200, ip,nw_dst=ip地址 actions=NORMAL"
处理ARP应答
ovs-ofctl add-flow s1 "table=0,priority=1,arp,nw_dst=10.0.0.1,actions=output:1"

ICMP应答处理
ovs-ofctl add-flow s1 "table=0,priority=0,actions=resubmit(,1)"
ovs-ofctl add-flow s1 "table=1,icmp,nw_dst=10.0.0.1,actions=mod_dl_dst=00:00:00:00:00:01,output:1"

 virsh -c qemu:///system list
  
  
vim ovs-ifup
vim ovs-ifdown
  
 
chmod 777 ovs-ifup 
chmod 777 ovs-ifdown
  
ovs-vsctl list
  
ovs-vsctl add-br lxbr0
ovs-vsctl add-port lxbr0 enp7s0
ovs-vsctl list-ports lxbr0
       

virsh list
virsh console id-of-vm

home/liuxin/odl#ls
gen



ovs-vsctl show 所有bridge

ovs-ofctl show bridge名字   查看bridge信息

ovs-ofctl dump-flows lxbr0  查看流表项

ovs-ofctl del-flows lxbr0   删除流表

ovs-ofctl add-flow lxbr0 actions=NORMAL

ovs-ofctl add-flow lxbr0 in_port=2,actions=output:4

ovs-vsctl list interface tapvm1w
```

```


1 kvm 建虚拟机

2 ovs 配置 网桥
ovs-ofctl add-flow lxbr0 "in_port=2,icmp actions=push:NXM_OF_ETH_DST[],pop:NXM_OF_ETH_SRC[],output:4"

两个虚机的ip处于相同网段时，OVS流表配置如下：
vm1的ip: 192.168.1.10，vm2的ip: 192.168.1.12  br-int 桥名
sudo ovs-ofctl add-flow br-int "ip,nw_dst=192.168.1.10 actions=output:2"
sudo ovs-ofctl add-flow br-int "ip,nw_dst=192.168.1.12 actions=output:4"
sudo ovs-ofctl add-flow br-int "arp,arp_tpa=192.168.1.10 actions=output:2"
sudo ovs-ofctl add-flow br-int "arp,arp_tpa=192.168.1.12 actions=output:4"


两个虚机的ip处于不同网段时，OVS流表配置如下：
vm1的ip: 10.0.0.10，网关: 10.0.0.1
vm2的ip: 10.0.10.11，网关: 10.0.10.1
sudo ovs-ofctl add-flow br-int "in_port=1,arp,arp_tpa=10.0.0.1,arp_op=1 actions=load:0x2->NXM_OF_ARP_OP[],move:NXM_NX_ARP_SHA[]->NXM_NX_ARP_THA[],load:0x5254008B9CB2->NXM_NX_ARP_SHA[],move:NXM_OF_ARP_SPA[]->NXM_OF_ARP_TPA[],load:0x0a000001->NXM_OF_ARP_SPA[],in_port"

sudo ovs-ofctl add-flow br-int "in_port=2,arp,arp_tpa=10.0.10.1,arp_op=1 actions=load:0x2->NXM_OF_ARP_OP[],move:NXM_NX_ARP_SHA[]->NXM_NX_ARP_THA[],load:0x5254004AADC2->NXM_NX_ARP_SHA[],move:NXM_OF_ARP_SPA[]->NXM_OF_ARP_TPA[],load:0x0a000a01->NXM_OF_ARP_SPA[],in_port"
辛仔
sudo ovs-ofctl add-flow br-int "in_port=1,icmp actions=push:NXM_OF_ETH_DST[],pop:NXM_OF_ETH_SRC[],mod_dl_dst:52:54:00:8B:9C:B2,output:2"
sudo ovs-ofctl add-flow br-int "in_port=2,icmp actions=push:NXM_OF_ETH_DST[],pop:NXM_OF_ETH_SRC[],mod_dl_dst:52:54:00:4A:AD:C2,output:1"



---------------------------------------
  https://feisky.gitbooks.io/sdn/ovs/
http://fishcried.com/2016-02-09/openvswitch-ops-guide/


ovs
ovs-appctl           ovs-dpctl            ovs-tcpdump
ovs-bugtool          ovs-dpctl-top        ovs-tcpundump
ovsdb-client         ovs-ofctl            ovs-vlan-test
ovsdb-server         ovs-parse-backtrace  ovs-vsctl
ovsdb-tool           ovs-pcap             ovs-vswitchd
ovs-docker           ovs-pki   

https://www.jianshu.com/p/f53a44d98ab2
OpenFlow(OVS)下的“路由技术”

tcpdump -i tapvm1w -vvv
ip a
--------------------------------------------
192.168.1.10  ping  192.168.2.10
【arp reply】 

ovs-ofctl add-flow lxbr0 table=0,in_port=2,arp,arp_tpa=192.168.1.1,arp_op=1,actions=move:"NXM_OF_ETH_SRC[]->NXM_OF_ETH_DST[]",load:"0x02->NXM_OF_ARP_OP[]",move:"NXM_NX_ARP_SHA[]->NXM_NX_ARP_THA[]",load:"0xfe:54:00:da:98:88->NXM_NX_ARP_SHA[]",move:"NXM_OF_ARP_SPA[]->NXM_OF_ARP_TPA[]",load:"0xc0a80101->NXM_OF_ARP_SPA[]",in_port


ovs-ofctl add-flow lxbr0 table=0,in_port=4,arp,arp_tpa=192.168.2.1,arp_op=1,actions=move:"NXM_OF_ETH_SRC[]->NXM_OF_ETH_DST[]",load:"0x02->NXM_OF_ARP_OP[]",move:"NXM_NX_ARP_SHA[]->NXM_NX_ARP_THA[]",load:"0xfe:54:00:5e:1c:52->NXM_NX_ARP_SHA[]",move:"NXM_OF_ARP_SPA[]->NXM_OF_ARP_TPA[]",load:"0xc0a80201->NXM_OF_ARP_SPA[]",in_port

两个虚机的ip处于不同网段时，OVS流表配置
vm1的ip: 192.168.1.10，网关: 192.168.1.1    port 2
vm3的ip: 192.168.2.10，网关: 192.168.2.1    port 3

ovs-ofctl add-flow lxbr0 "in_port=2,arp,arp_tpa=192.168.1.1,arp_op=1 actions=load:0x2->NXM_OF_ARP_OP[],move:NXM_NX_ARP_SHA[]->NXM_NX_ARP_THA[],load:0xfe5400da9888->NXM_NX_ARP_SHA[],move:NXM_OF_ARP_SPA[]->NXM_OF_ARP_TPA[],load:0xc0a80101->NXM_OF_ARP_SPA[],in_port"
1.1 mac

ovs-ofctl add-flow lxbr0 "in_port=2,icmp actions=push:NXM_OF_ETH_DST[],pop:NXM_OF_ETH_SRC[],mod_dl_dst:fe:54:00:da:98:88,output:3"
2.10 mac

ovs-ofctl add-flow lxbr0 "in_port=3,arp,arp_tpa=192.168.2.1,arp_op=1 actions=load:0x2->NXM_OF_ARP_OP[],move:NXM_NX_ARP_SHA[]->NXM_NX_ARP_THA[],load:0xfe54005e1c52->NXM_NX_ARP_SHA[],move:NXM_OF_ARP_SPA[]->NXM_OF_ARP_TPA[],load:0xc0a80201->NXM_OF_ARP_SPA[],in_port"
2.1 mac

ovs-ofctl add-flow lxbr0 "in_port=3,icmp actions=push:NXM_OF_ETH_DST[],pop:NXM_OF_ETH_SRC[],mod_dl_dst:fe:54:00:5e:1c:52,output:2"
1.10 mac

两个虚机的ip处于不同网段时，OVS流表配置

move:"NXM_OF_ETH_SRC[]->NXM_OF_ETH_DST[]" 将请求的源mac作为reply的目标mac
mod_dl_src:"02:ac:10:ff:01:01" 修改reply的源mac为虚拟网关的mac
load:"0x02->NXM_OF_ARP_OP[]" 修改arp包类型为reply包
move:"NXM_NX_ARP_SHA[]->NXM_NX_ARP_THA[]" 将request包中的源mac赋值给reply的目标mac
load:"0x02ac10ff0101->NXM_NX_ARP_SHA[]" 设置reply的源mac
move:"NXM_OF_ARP_SPA[]->NXM_OF_ARP_TPA[]" 将request包中的源ip赋值给reply的目标ip
load:"0x0a000001->NXM_OF_ARP_SPA[]" 设置reply包的源ip 为虚拟网关的ip，格式为十进制转换为对应的16进制
in_port 从进入端口发回去

【icmp reply】

ovs-ofctl add-flow lxbr0 table=0,in_port=2,icmp,nw_dst=192.168.2.10,icmp_type=8,icmp_code=0,actions=push:"NXM_OF_ETH_SRC[]",push:"NXM_OF_ETH_DST[]",pop:"NXM_OF_ETH_SRC[]",pop:"NXM_OF_ETH_DST[]",push:"NXM_OF_IP_SRC[]",push:"NXM_OF_IP_DST[]",pop:"NXM_OF_IP_SRC[]",pop:"NXM_OF_IP_DST[]",load:"0xff->NXM_NX_IP_TTL[]",load:"0->NXM_OF_ICMP_TYPE[]",output:4,mod_dl_dst:fe:54:00:da:98:88

ovs-ofctl add-flow lxbr0 table=0,in_port=4,icmp,nw_dst=192.168.1.10,icmp_type=8,icmp_code=0,actions=push:"NXM_OF_ETH_SRC[]",push:"NXM_OF_ETH_DST[]",pop:"NXM_OF_ETH_SRC[]",pop:"NXM_OF_ETH_DST[]",push:"NXM_OF_IP_SRC[]",push:"NXM_OF_IP_DST[]",pop:"NXM_OF_IP_SRC[]",pop:"NXM_OF_IP_DST[]",load:"0xff->NXM_NX_IP_TTL[]",load:"0->NXM_OF_ICMP_TYPE[]",output:2,mod_dl_dst:fe:54:00:5e:1c:52


output:port	输出数据包到指定的端口。port 是指端口的 OpenFlow 端口编号
mod_vlan_vid	修改数据包中的 VLAN tag
strip_vlan	移除数据包中的 VLAN tag
mod_dl_src/ mod_dl_dst	修改源或者目标的 MAC 地址信息
mod_nw_src/mod_nw_dst	修改源或者目标的 IPv4 地址信息
resubmit:port	替换流表的 in_port 字段，并重新进行匹配
load:value−>dst[start..end]	写数据到指定的字段

arp_tpa 目标ip


【ovs-ofctl show lxbr0】
 2(tapvm1w): addr:fe:54:00:5e:1c:52
     config:     0
     state:      0
     current:    10MB-FD COPPER
     speed: 10 Mbps now, 0 Mbps max
 3(tapvm3w): addr:fe:54:00:da:98:88
     config:     0
     state:      0
     current:    10MB-FD COPPER
     speed: 10 Mbps now, 0 Mbps max

```
