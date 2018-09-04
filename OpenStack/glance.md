[深入镜像服务Glance](https://www.cnblogs.com/sammyliu/p/4249151.html)

```
image 的各种状态

queued：没有上传 image 数据，只有db 中的元数据。
saving：正在上传 image data
active：正常状态
deleted/pending_delete： 已删除/等待删除
killed：image 元数据不正确，等待被删除。



操作流程
命令
image-create
image-update
glance image-list
glance image-show id号
```
