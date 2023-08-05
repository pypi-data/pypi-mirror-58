
from hupload.upload import Storage
from qiniu import Auth, put_file, etag
from qiniu import BucketManager
import os

"""
 * 七牛存储器
 *<B>说明：</B>
 *<pre>
 *  略
 *</pre>
 *<B>示例：</B>
 *<pre>
 * 略
 *</pre>
 *<B>日志：</B>
 *<pre>
 *  略
 *</pre>
 *<B>注意事项：</B>
 *<pre>
 *  略
 *</pre>
"""
class QiniuStorage(Storage):

    def __init__(self, **attrs):

        # 七牛accessKey
        # <B> 说明： </B>
        # <pre>
        # 略
        # </pre>
        self.accessKey = '';

        # 七牛secretKey
        # <B> 说明： </B>
        # <pre>
        # 略
        # </pre>
        self.secretKey = '';

        # 七牛权限控制对象
        # <B> 说明： </B>
        # <pre>
        # 略
        # </pre>
        self.auth = None;

        # 七牛bucket对象
        # <B> 说明： </B>
        # <pre>
        # 略
        # </pre>
        self.bucketManager = None

        # 默认bucket
        # <B> 说明： </B>
        # <pre>
        # 略
        # </pre>
        self.bucket = '';

        # oss directpoint
        # <B> 说明： </B>
        # <pre>
        # 直传地址(直接通过客户端浏览器上传)
        # </pre>
        self.directurl = '';

        # oss client
        # <B> 说明： </B>
        # <pre>
        # 略
        # </pre>
        self.ossClient = None;

        super().__init__(**attrs)

        return ;


    def getAuth(self)->'Auth':

        if self.auth:
            return self.auth

        self.auth = Auth(self.accessKey,self.secretKey, )

        return self.auth;


    def getBucketManager(self)->'BucketManager':

        if self.bucketManager:
            return self.bucketManager
        auth = self.getAuth();
        self.bucketManager = BucketManager(auth);

        return self.bucketManager;

    def saveInternal(self,file,allowExts = [],**options):
        try :
            auth = self.getAuth()
            key = file['filepath']
            bucket = options.get("bucket",self.bucket)
            token = auth.upload_token(bucket, key, 3600)
            ret, info = put_file(token, key,  file['tmp_name'])
            if ret['key'] != key:
                return False

            return file

        except Exception as e:
            self.uploadManager.setError(str(e))
            return False;

        return False;

    def filesInternal(self,dir,allowExts = [], **options):

        try :

            bucketManager = self.getBucketManager()
            bucket_name = options.get("bucket", self.bucket)

            if dir[-1] != '/':
                prefix = dir + '/'
            else:
                prefix = dir;

            marker = options.get("marker","")
            limit = options.get("limit", 1000)
            delimiter = None
            ret, eof, info = bucketManager.list(bucket_name, prefix, marker, limit, delimiter)
            newFiles = [];
            for obj in ret.get('items'):
                file = {};
                key = obj['key']
                file['filename'] = os.path.basename(key);
                file['filepath'] = key;
                ext = os.path.splitext(key)[1][1:]
                # 文件扩展名
                if allowExts and ext not in allowExts:
                    continue;

                file['isdir'] = False;
                newFiles.append(file)

            return {"items":newFiles,"marker":eof};

        except Exception as e:
            self.uploadManager.setError(str(e))
            return False;

        return False;

    def deleteInternal(self, filepath, **options):

        try:
            bucketManager = self.getBucketManager()
            bucket_name = options.get("bucket", self.bucket)

            ret, info = bucketManager.delete(bucket_name, filepath)
            if ret == {}:
                return True
            else:
                return False

        except Exception as e:
            self.uploadManager.setError(str(e))
            return False;

        return False;


    def postInternal(self,file:dict,**options):

        bucket_name = options.get("bucket", self.bucket)
        expire = options.get('expire', 60 * 30);
        policy = options.get("policy",{"scope":"<bucket>:<key>"})

        auth = self.getAuth()
        key = file['filepath']
        token = auth.upload_token(bucket_name, key, expire,policy)
        #crc = file_crc32(file_path)
        response = {
            'action':self.directurl,
            'key':key,
            'x:<custom_name>':'',
            'token':token,
            'accept':''
        };

        return response;











