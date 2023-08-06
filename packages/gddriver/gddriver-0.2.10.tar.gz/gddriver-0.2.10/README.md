# gddriver

[![pipeline status](http://gitlab.genedock.com/genedock/gddriver/badges/master/pipeline.svg)](http://gitlab.genedock.com/genedock/gddriver/commits/master)
[![coverage report](http://gitlab.genedock.com/genedock/gddriver/badges/master/coverage.svg)](http://gitlab.genedock.com/genedock/gddriver/commits/master)

存储驱动：封装oss/ftp等底层存储服务的api

## 快速开始

### 使用oss驱动进行操作

```python
import gddriver

from gddriver import models
from gddriver import providers


host = "https://oss-cn-shenzhen.aliyuncs.com"
port = None  # oss无需填端口号
container_name = 'bucket name'
credential = models.Credential(
    access_key_id="",
    access_key_secret="",
    access_key_token=""
)


# operator 支持使用with的上下文，在每次使用之后释放资源
with gddriver.GenericOperator(
                provider=providers.Provider.OSS, credential=credential,
                host=host,port=port) as operator:
    obj_list, next_marker = operator.list_container_objects(container_name=container_name)
    for i in obj_list:
        print(i)
```

### 使用ftp驱动进行操作

```python
import gddriver

from gddriver import models
from gddriver import providers


host = "127.0.0.1"
port = 21
container_name = 'bucket name'
credential = models.Credential(
    user="",
    password="",
)


# operator 支持使用with的上下文，在每次使用之后释放资源
with gddriver.GenericOperator(
                provider=providers.Provider.FTP, 
                credential=credential,host=host,port=port) as operator:
    obj_list, next_marker = operator.list_container_objects(container_name=container_name)
    for i in obj_list:
        print(i)
```

### 自定义分片上传

```python
# -*- coding: utf-8 -*-

from gddriver import Provider
from gddriver import transmission
from gddriver import models


container_name = "your bucket or ftp directory"
credential = models.Credential(
    access_key_id="your access key id",
    access_key_secret="your access key secret",
    user='user name',
    password='password'
)

operator = transmission.GenericOperator(
    host="endpoint",
    credential=credential,
    port=None,
    provider=Provider.OSS  # Provider.FTP
)


object_name = "sample/test-multi"
upload_id = operator.init_multipart_upload(
        container_name=container_name,
        object_name=object_name
)

with open("/path/to/file", "rb") as f:
    part_num = 0
    parts = []
    while True:
        part_num += 1
        # oss 最小分片要求100KB
        c = f.read(1024 * 100)
        if not c:
            break

        part_upload_request = models.PartUploadRequest(
            container_name=container_name,
            stream=c,
            object_name=object_name,
            part_number=part_num,
            upload_id=upload_id
        )
        # 注意：ftp等存储介质下，operator不是线程安全的
        result = operator.upload_part(request=part_upload_request)
        # 等价
        # parts.append({"etag": result.part_info.etag, "part_number": result.part_info.part_number})
        parts.append(result.part_info)
    print("Parts: {}".format(parts))

    request = models.CompleteMultipartUploadRequest(
        container_name=container_name,
        object_name=object_name,
        upload_id=upload_id,
        parts=parts
    )
    operator.complete_multipart_upload(request=request)

```



## 模块说明

### models.Object

文件/对象的原信息，包含name, size等基础信息以及`extra`字典中包含的额外信息

`extra`中（可能包含）的信息在不同的存储中实现如下：

* oss:
    * last_modified:    UNIX TIMPSTAMP
    * etag：            etag
    * object_type:      Normal Multipart Appendable ...
    * storage_class:    Standard Archive ...
    * restore:          是否为恢复/恢复中的归档文件 （get_object_meta时获得）
    * restore_finished: 是否恢复完成  （get_object_meta时获得）
    * expiry_date:      归档文件恢复的过期时间 （get_object_meta时获得）
* ftp:
    * parent:         /root/prefix
    * is_file:        是否为文件
    * short_name:     对象名，没有前缀


`storage_class`属性获取文件在对象存储中的类型，如 `Standard` `Archived`等，依据存储介质而定，默认为`Standard`


### models._Request

存储服务操作请求

* _Request
    * StreamTransferRequest 流式（上传）请求
        * FTPStreamUploadRequest ftp流式上传
        * OSSStreamUploadRequest oss流式上传
        * AppendRequest 追加上传
        * PartUploadRequest 分片上传
    * FileTransferRequest 文件传输请求
        * OSSUploadRequest oss文件上传
        * FTPUploadRequest ftp文件上传
        * OSSDownloadRequest oss文件下载
        * FTPDownloadRequest ftp文件下载
    * CopyRequest 复制请求
        * OSSCopyRequest oss文件复制请求
    * StreamDownloadRequest 流式下载请求
        * FTPStreamDownloadRequest ftp流式下载
        * OSSStreamDownloadRequest oss流式下载

### models.OperationResult

部分请求返回的操作结果，以下接口返回的值为`OperationResult`的子类对象：

* upload_file 
* upload_object_via_stream 
* append_object 
* download_file 
* download_object_as_stream 
* restore_object 
* upload_part 
* complete_multipart_upload

部分模型的介绍：
* DownloadResult   下载结果，包含`server_checksum` `client_checksum` `checksum_type`等信息
* StreamDownloadResult  一个可迭代对象，同时包含`stream`（类File的流）和`client_checksum`（需要完成流的读取之后才能获得）属性
* UploadResult  上传结果，包含`checksum` `checksum_type`等信息
    * AppendResult 追加上传的结果, `checksum`为追加上传这一部分的校验码
* RestoreResult  归档文件恢复的结果，包含`finished`(是否完成)和`expiry_date`(过期时间)属性
* PartUploadResult 分片上传结果，包含`part_info`属性，用于完成分片上传请求


### models.Credential

Credential用于管理存储服务的认证信息，`user`, `password`, `access_key_id`, `access_key_secret`, `access_key_token` 等信息

### base.Connection

存储服务的连接信息，使用驱动执行操作时，需要通过Connection对象创建连接、发送请求等，不同的服务有不同的实现方式

* drivers.ftp.FTPConnection
* drivers.ftp.OSSConnection


### base.StorageDriver

定义了访问存储介质时的操作接口：

* 上传
    * 上传本地文件
    * 通过流上传
    * 追加上传（追加上传只能以流的形式上传）
* 下载
    * 下载到本地文件
    * 以流的形式下载
* 删除
    * 删除对象
    * 通过前缀删除（部分实现）
    * 批量删除（部分实现）
* 冷备、恢复
* 获取前面链接
* 遍历`container`中的对象/文件
* 初始化`Connection`实例


> `StorageDriver`对象是线程安全的：`StorageDriver`的所有实现，都只是"定义"了在这种存储介质下操作的行为方式，所有的操作都基于函数传入的`connection`参数，并不会管理用户的`Connection`信息

