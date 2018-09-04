参考
http://forum.openedgecomputing.org/t/a-failure-in-creating-a-vm-overlay/15/4?u=linuix
```
自己下载的小镜像
【root@cloudlet:~# source admin-openrc.sh  
【http://download.cirros-cloud.net/0.3.3/cirros-0.3.3-x86_64-disk.img
【root@cloudlet:~# cloudlet base /var/lib/libvirt/images/cirros-0.3.3-x86_64-disk.img
INFO     save VM memory state
DEBUG    start machine save
INFO     Header size of memory snapshot is 8192
[================================================================================>] 100%
DEBUG    finish machine save
INFO     Start Base VM Memory hashing
INFO     Get hash list of memory page
[===============================================================================>.] 99%
DEBUG    FREE Memory Counter: 0(0)
INFO     Finish Base VM Memory hashing
INFO     Start Base VM Disk hashing
[================================================================================>] 100%INFO     Finish Base VM Disk hashing
Base VM is created from /var/lib/libvirt/images/cirros-0.3.3-x86_64-disk.img
Disk: /var/lib/libvirt/images/cirros-0.3.3-x86_64-disk.img
Mem: /var/lib/libvirt/images/cirros-0.3.3-x86_64-disk.base-mem

【root@cloudlet:~# cloudlet list-base
hash value                                      path
------------------------------------------------------------------------------------------
6bd9268b1b4539b21443a702b23987a6a164c6db199ef72e6f30f0fdc674bbd5        /var/lib/libvirt/images/cirros-0.3.3-x86_64-disk.img
------------------------------------------------------------------------------------------

【root@cloudlet:~# cloudlet export-base /var/lib/libvirt/images/cirros-0.3.3-x86_64-disk.img my_create_basevm.zip
INFO     Start compressing
INFO     zip -j -9 ./my_create_basevm.zip.zip /var/lib/libvirt/images/cirros-0.3.3-x86_64-disk.img /var/lib/libvirt/images/cirros-0.3.3-x86_64-disk.base-mem /var/lib/libvirt/images/cirros-0.3.3-x86_64-disk.base-img-meta /var/lib/libvirt/images/cirros-0.3.3-x86_64-disk.base-mem-meta
  adding: cirros-0.3.3-x86_64-disk.img (deflated 12%)
  adding: cirros-0.3.3-x86_64-disk.base-mem (deflated 100%)
  adding: cirros-0.3.3-x86_64-disk.base-img-meta (deflated 16%)
  adding: cirros-0.3.3-x86_64-disk.base-mem-meta (deflated 94%)

【root@cloudlet:~# ls
admin-openrc.sh      glancedb.sql    keystonedb.sql            novadb.sql  视频  下载
elijah-openstack     heatdb.sql      l-clet                    公共的      图片  音乐
elijah-provisioning  heat-domain.sh  my_create_basevm.zip.zip  模板        文档  桌面

【root@cloudlet:~# cloudlet import-base my_create_basevm.zip.zip
Traceback (most recent call last):
  File "/usr/local/bin/cloudlet", line 376, in <module>
    status = main(sys.argv)
  File "/usr/local/bin/cloudlet", line 323, in main
    PackagingUtil.import_basevm(import_file)
  File "/usr/local/lib/python2.7/dist-packages/elijah/provisioning/package.py", line 626, in import_basevm
    raise ImportBaseError(msg)
elijah.provisioning.package.ImportBaseError: Base VM is already exists. Delete existing Base VM using command. See more 'cloudlet --help'

【root@cloudlet:~# cloudlet overlay /var/lib/libvirt/images/cirros-0.3.3-x86_64-disk.img
INFO     QEMU access file : /tmp/cloudlet-qemu-CLqb0z/qemu-trim-log
INFO     start monitoring at /var/tmp/cloudletfs-uNzi9h/disk/streams/chunks_modified
INFO     start monitoring at /var/tmp/cloudletfs-uNzi9h/disk/streams/chunks_accessed
INFO     start monitoring at /var/tmp/cloudletfs-uNzi9h/memory/streams/chunks_accessed
INFO     start monitoring at /tmp/cloudlet-qemu-CLqb0z/qemu-trim-log
INFO     * Overlay creation configuration
INFO       - {'DISK_ONLY': False,
 'FREE_SUPPORT': False,
 'TRIM_SUPPORT': True,
 'XRAY_SUPPORT': False,
 'ZIP_CONTAINER': True}
INFO     restoring VM...
INFO     VM is restored...
INFO     waiting for finishing VNC interaction
INFO     stop monitoring at /var/tmp/cloudletfs-uNzi9h/memory/streams/chunks_accessed
INFO     save VM memory state
DEBUG    start machine save
INFO     Header size of memory snapshot is 8192
[================================================================================>] 100%
DEBUG    finish machine save
WARNING  No TRIM Discard, Check /etc/fstab configuration
INFO     Get memory delta
DEBUG    1.get modified page list
INFO     Get hash list of memory page
[===============================================================================>.] 99%
DEBUG    FREE Memory Counter: 0(0)
INFO     Get disk delta
DEBUG    1.get modified disk page
DEBUG    1-1. Trim(0, overwritten after trim(0)), Xray(0)
INFO     Generate VM overlay using deduplication
DEBUG    2-1.Find zero page
DEBUG    matching (0/8) with base
DEBUG    2-2.get delta from base Memory
DEBUG    matching (0/8) with base
DEBUG    2-3.get delta from base Disk
DEBUG    matching (0/8) with base
DEBUG    3.get delta from itself
DEBUG    self delta : 0/8
INFO     Print statistics
INFO     --------------------------------------------------
INFO     Total Modified Disk #     : 0  ( 100 %, 0.000000 MB )
INFO     No disk modification
INFO     Total Modified Memory #  : 8   ( 100 %, 0.000657 MB)
INFO     FREE discard             : 0   ( 0.000000 % )
INFO     Zero pages               : 0   ( 0.000000 % )
INFO     Shared with Base Disk    : 0   ( 0.000000 % )
INFO     Shared with Base Mem     : 0   ( 0.000000 % )
INFO     Shared within Self       : 0   ( 0.000000 % )
INFO     Shared with Overlay Disk : 0   ( 0.000000 % )
INFO     Shared with Overlay Mem  : 0   ( 0.000000 % )
INFO     xdelta                   : 8   ( 100.000000 %, real_size: 537 KB )
INFO     raw                      : 0   ( 0.000000 %, real_size: 0 KB )
INFO     --------------------------------------------------
INFO     [LZMA] Compressing overlay blobs (/tmp/cloudlet-overlay-YR7U76/overlay-meta)
DEBUG    Overlay Compression time: 0.438746, delta_item: 8
DEBUG    Total Overlay Size : 580
INFO     close Stream monitoring thread
INFO     Fuse close pipe
INFO     NO chunks has been waited at FUSE
INFO     close Fuse Exec thread
INFO     close File monitoring thread
meta file : (272) bytes
blob file : (580) bytes (overlay-blob_1.xz)
zip overhead : (251) bytes
overlay file at : /tmp/cloudlet-overlay-YR7U76/overlay.zip

【root@cloudlet:~# cloudlet synthesis /var/lib/libvirt/images/cirros-0.3.3-x86_64-disk.img /tmp/cloudlet-overlay-YR7U76/overlay.zip
DEBUG    ==========================================
DEBUG    file:///tmp/cloudlet-overlay-YR7U76/overlay.zip
INFO     Decompression time : 0.000756 (s)
INFO     Recovering launch VM
INFO     Start FUSE (0.328714 s)
DEBUG    Overlay has 8 chunks
INFO     Resume the launch VM
INFO     QEMU access file : /tmp/cloudlet-overlay-DEagEc/qemu-trim-log
INFO     QEMU access file : /tmp/cloudlet-overlay-DEagEc/qmp-channel
INFO     Launch disk: /tmp/cloudlet-launch-disk-R94nKJ
INFO     Launch memory: /tmp/cloudlet-launch-mem-b9SdkX
INFO     QMP channel: /tmp/cloudlet-overlay-DEagEc/qmp-channel
INFO     start monitoring at /var/tmp/cloudletfs-M5sM94/disk/streams/chunks_modified
INFO     start monitoring at /var/tmp/cloudletfs-M5sM94/disk/streams/chunks_accessed
INFO     start monitoring at /var/tmp/cloudletfs-M5sM94/memory/streams/chunks_accessed
INFO     start monitoring at /tmp/cloudlet-overlay-DEagEc/qemu-trim-log
INFO     [Delta] Handle dangling DeltaItem (0)
DEBUG    Delta metrics: 
DEBUG    ==================================================
DEBUG    Counter({32: 8, 'sha': 8})
DEBUG    Counter({'sha': 0.0006613731384277344, 'unpack': 0.0006473064422607422, 32: 0.00042724609375, 'seekwrite': 4.100799560546875e-05, 'dict': 2.6941299438476562e-05, 'flush': 2.1696090698242188e-05})
DEBUG    Total captured time: 0
INFO     [Delta] : (1533638587.27)-(1533638587.27)=(0.00764179229736), delta 8 chunks
INFO     [FUSE] : (1533638587.27)-(1533638587.27)=(0.00485587120056)

DEBUG    File closing time for recover memory snapshot: 0.000247
INFO     restoring VM...
INFO     VM is restored...
INFO     [RESUME] : QEMU resume time (1533638587.402287)~(1533638587.736787)=(0.334500)
INFO     waiting for finishing VNC interaction
INFO     close Stream monitoring thread
INFO     Fuse close pipe
INFO     NO chunks has been waited at FUSE
INFO     close Fuse Exec thread
INFO     close File monitoring thread

```

```
乐高镜像
【root@cloudlet:~# cloudlet import-base /root/lx/ubuntu-trusty-lego-base.zip
INFO     create directory for base VM
INFO     Decompressing Base VM to temp directory at /tmp/cloudlet-base-PW3_hp
INFO     Place base VM to a right directory
INFO     Register New Base to DB
INFO     ID for the new Base VM: a8157d3eb1155ec13b80615afc883b5f01f99362214f72f2b6444854498d7b17
INFO     Success

【root@cloudlet:~# cloudlet list-base
hash value                                      path
------------------------------------------------------------------------------------------
a8157d3eb1155ec13b80615afc883b5f01f99362214f72f2b6444854498d7b17        
/root/.cloudlet/a8157d3eb1155ec13b80615afc883b5f01f99362214f72f2b6444854498d7b17/trusty-server-raw.img
------------------------------------------------------------------------------------------

【root@cloudlet:~# cloudlet synthesis /root/.cloudlet/a8157d3eb1155ec13b80615afc883b5f01f99362214f72f2b6444854498d7b17/
trusty-server-raw.img    /root/lx/overlay.zip

DEBUG    ==========================================
DEBUG    file:///root/lx/overlay.zip
INFO     Decompression time : 41.311197 (s)
INFO     Recovering launch VM
INFO     Start FUSE (1.291393 s)
DEBUG    Overlay has 427089 chunks
INFO     Resume the launch VM
INFO     QEMU access file : /tmp/cloudlet-overlay-bq8LYR/qemu-trim-log
INFO     QEMU access file : /tmp/cloudlet-overlay-bq8LYR/qmp-channel
INFO     Launch disk: /tmp/cloudlet-launch-disk-0VkruI
INFO     Launch memory: /tmp/cloudlet-launch-mem-Tx2hYC
INFO     QMP channel: /tmp/cloudlet-overlay-bq8LYR/qmp-channel
INFO     start monitoring at /var/tmp/cloudletfs-NYpdAe/disk/streams/chunks_modified
INFO     start monitoring at /var/tmp/cloudletfs-NYpdAe/disk/streams/chunks_accessed
INFO     start monitoring at /var/tmp/cloudletfs-NYpdAe/memory/streams/chunks_accessed
INFO     start monitoring at /tmp/cloudlet-overlay-bq8LYR/qemu-trim-log
INFO     [Delta] Handle dangling DeltaItem (0)
DEBUG    Delta metrics: 
DEBUG    ==================================================
DEBUG    Counter({'sha': 427089, 32: 164516, 48: 144128, 16: 59044, 80: 49869, 64: 8304, 96: 1228})
DEBUG    Counter({32: 1711.0312843322754, 80: 118.52115035057068, 64: 104.98860192298889, 'unpack': 35.44292974472046, 
'sha': 20.44668459892273, 'dict': 4.128907203674316, 'seekwrite': 1.6258974075317383, 'flush': 0.8647711277008057,
48: 0.6096794605255127, 16: 0.09760212898254395, 96: 0.0017435550689697266})
DEBUG    Total captured time: 1997
INFO     [Delta] : (1533647921.51)-(1533650262.78)=(2341.27055907), delta 427089 chunks
INFO     [FUSE] : (1533647921.51)-(1533650262.78)=(2341.26941895)

DEBUG    File closing time for recover memory snapshot: 0.000579
INFO     restoring VM...
INFO     VM is restored...
INFO     [RESUME] : QEMU resume time (1533650264.352120)~(1533650266.354378)=(2.002258)
INFO     waiting for finishing VNC interaction
INFO     close Stream monitoring thread
INFO     Fuse close pipe
INFO     NO chunks has been waited at FUSE
INFO     close Fuse Exec thread
INFO     close File monitoring thread

```
