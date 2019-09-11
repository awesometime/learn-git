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

```
