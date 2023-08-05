# hehey-hupload 上传组件

#### 介绍
hehey-hupload 是一个python 文件上传工具类.
支持:
  - 本地上传
  - 阿里云对象存储(oss)
  - 腾讯云对象存储(cos)
  - 起牛云对象存储(qiniu)
  
  
#### 参数配置
```python
conf =  {
            'clazz': 'hupload.upload.UploadManager',
            'defaultStorage': 'oss',# 默认上传存储
            'customStorages': {
                # 本地上传存储配置
                'local': {
                    'clazz': 'hupload.storages.LocalStorage.LocalStorage',
                    'rootPath': "/home/hehe/www/upload"
                },
                # 阿里云oss上传存储配置
                'oss': {
                    'clazz': 'hupload.storages.OssStorage.OssStorage',
                    'bucket': "",
                    "accessId":"",
                    "secretKey": "",
                    "endpoint": "http://oss-cn-hangzhou.aliyuncs.com",
                    "directurl": "",
                },
                # 七牛上传存储配置
                'qiniu': {
                    'clazz': 'hupload.storages.QiniuStorage.QiniuStorage',
                    'bucket': "upload",
                    "accessKey": "",
                    "secretKey": "",
                    "directurl":"http://up.qiniu.com"

                },
                 # 腾讯云上传存储配置
                'cos': {
                    'clazz': 'hupload.storages.CosStorage.CosStorage',
                    'bucket': "",
                    'region':"ap-shanghai",
                    "secretId": "",
                    "secretKey": "",
                    "directurl": ""
                }

            },
        },
```

#### 基本示例

- 快速使用
```python
from hupload.upload import UploadManager;
conf = {

};
hupload = UploadManager(conf)

# 上传本地文件
file = hupload.uploadFile("/home/hehe/doc/9921521429915_.pic.jpg","temp/test")
# 上传表单的文件
file = {"tmp_name":"/tmp/9921521429915.jpg"};
file = hupload.uploadFile(file,"temp/test")
# 读取文件temp/test 目录下的所有文件
hupload.getFiles("temp/test")
# 删除文件
hupload.deleteFile("temp/test/b51f82ff03511154a5d6d27b1391a61911.jpg")


```


- 上传本地文件
```python
from hupload.upload import UploadManager;
conf = {

};
hupload = UploadManager(conf)

# 上传本地文件:/home/hehe/doc/9921521429915_.pic.jpg,指定上传目录:temp/test
file = hupload.uploadFile("/home/hehe/doc/9921521429915_.pic.jpg","temp/test/xxx.jpg")

```

- 上传表单文件
```python
from hupload.upload import UploadManager;
conf = {

};
hupload = UploadManager(conf)

# 一般需结合web 的 文件域数据结构
file = {
 'temp_name':"/tmp/b51f82ff03511154a5d6d27b1391a61911.jpg"
};

file = hupload.uploadFile(file,"temp/test")

```

- 表单直传(并未直接上传,而是生成web 浏览器上传需要的参数)
```python
from hupload.upload import UploadManager;
conf = {

};
hupload = UploadManager(conf)

file = hupload.directFile("test.jpeg","temp/test")

# file 基本格式,action 为表单的上传地址,其他为表单的隐藏域参数

{

    'key':'2019/12/20/7334af3394db452e9819d4a39148830c.jpeg',
    'OSSAccessKeyId':'',
    'signature':'zZ8zk784KTiurn3cb1tuCSAu4LQ=',
    'action':'http://yesmba-test.oss-cn-hangzhou.aliyuncs.com',
    'expire':1576823234,
    'policy':'eyJleHBpcmF0aW9uIjogIjIwMTktMTItMjBUMTQ6Mjc6MTQuMDAwWiIsICJjb25kaXRpb25zIjogW1siY29udGVudC1sZW5ndGgtcmFuZ2UiLCAwLCAxMDQ4NTc2MDAwXSwgWyJzdGFydHMtd2l0aCIsICIyMDE5LzEyLzIwLzczMzRhZjMzOTRkYjQ1MmU5ODE5ZDRhMzkxNDg4MzBjLmpwZWciLCAiMjAxOS8xMi8yMCJdXX0='

}

```

- 上传base64文件
```python
from hupload.upload import UploadManager;
conf = {

};
hupload = UploadManager(conf)

# 构建文件base64数据
base64_data = hupload.buildBase64("/home/hehe/图片/5a7c026e1026d.jpg")


# 上传base64 数据
hupload.uploadBase64(base64_data,'temp/test/base64.png')

```

- 下载远程文件并上传
```python
from hupload.upload import UploadManager;
conf = {

};
hupload = UploadManager(conf)

downloadUrl = "http://cms-bucket.ws.126.net/2019/12/20/ad40965d27b34414bf8413454fe076cf.jpeg?imageView&thumbnail=380y187&quality=85"

file = hupload.downloadAndUpload(downloadUrl,"'temp/test/downloadUrl.png'")

```

- 批量上传
```python
from hupload.upload import UploadManager;
conf = {

};

hupload = UploadManager(conf)

files = [
  '/tmp/b51f82ff03511154a5d6d27b1391a61911.jpg',
  '/tmp/b51f82ff03511154a5d6d27b1391a61911.jpg',
];

files = hupload.uploadAll(files,"temp/test/")

```

- 读取文件
```python
from hupload.upload import UploadManager;
conf = {

};

hupload = UploadManager(conf)

# 读取temp/test/ 目录下所有文件包括目录
hupload.getFiles("temp/test/")

```


- 删除文件
```python
from hupload.upload import UploadManager;
conf = {

};

hupload = UploadManager(conf)
result = hupload.deleteFile("temp/test/b51f82ff03511154a5d6d27b1391a61911.jpg")

```


- 获取上传存储对象
```python
from hupload.upload import UploadManager;
conf = {

};

hupload = UploadManager(conf)

# 获取oss 上传存储对象
hupload.oss.uploadFile("/home/hehe/doc/9921521429915_.pic.jpg","temp/test/xxx.jpg")


```

- 上传错误信息
```python
from hupload.upload import UploadManager;
conf = {

};

hupload = UploadManager(conf)

file = hupload.uploadFile("/home/hehe/doc/9921521429915_.pic.jpg","temp/test/xxx.jpg")
if not file:
    print(hupload.getError())


```
