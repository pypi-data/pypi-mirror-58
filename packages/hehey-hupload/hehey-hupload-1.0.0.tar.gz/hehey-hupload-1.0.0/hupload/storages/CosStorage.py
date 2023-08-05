
from hupload.upload import Storage
from qcloud_cos import CosConfig
from qcloud_cos import CosS3Client
import os
import time;

"""
 * 腾讯云存储器
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
class CosStorage(Storage):

    def __init__(self, **attrs):

        # cos accessId
        # <B> 说明： </B>
        # <pre>
        # 略
        # </pre>
        self.secretId = '';

        # cos secretKey
        # <B> 说明： </B>
        # <pre>
        # 略
        # </pre>
        self.secretKey = None;

        # 默认bucket
        # <B> 说明： </B>
        # <pre>
        # 略
        # </pre>
        self.bucket = '';

        # 区域
        # <B> 说明： </B>
        # <pre>
        # 略
        # </pre>
        self.region = 'tj'

        # cos directpoint
        # <B> 说明： </B>
        # <pre>
        # 直传地址(直接通过客户端浏览器上传)
        # </pre>
        self.directurl = '';

        # cos client
        # <B> 说明： </B>
        # <pre>
        # 略
        # </pre>
        self.cosClient = None;

        super().__init__(**attrs)

        return ;


    def getCosClient(self)->'CosS3Client':

        if self.cosClient:
            return self.cosClient

        token = None  # 使用临时密钥需要传入 Token，默认为空，可不填
        scheme = 'https'  # 指定使用 http/https 协议来访问 COS，默认为 https，可不填
        config = CosConfig(Region=self.region, SecretId=self.secretId, SecretKey=self.secretKey, Token=token, Scheme=scheme)
        # 2. 获取客户端对象
        self.cosClient = CosS3Client(config)

        return self.cosClient;

    def saveInternal(self,file,allowExts = [],**options):
        try :
            client = self.getCosClient()
            key = file['filepath']
            bucket_name = options.get("bucket", self.bucket)
            with open(file['tmp_name'], 'rb') as fp:
                response = client.put_object(
                    Bucket=bucket_name,
                    Body=fp,
                    Key=key,
                    StorageClass='STANDARD',
                    EnableMD5=False
                )

            if response and isinstance(response,dict):
                return file

            return False;

        except Exception as e:
            self.uploadManager.setError(str(e))
            return False;

        return False;

    def filesInternal(self,dir,allowExts = [], **options):

        try :

            client = self.getCosClient()
            bucket_name = options.get("bucket", self.bucket)
            if dir[-1] != '/':
                prefix = dir + '/'
            else:
                prefix = dir;

            marker = options.get("marker","")
            limit = options.get("limit", 1000)
            delimiter = ""
            response = client.list_objects(
                Bucket=bucket_name,
                Prefix=prefix,
                Marker=marker,
                MaxKeys=limit,
                Delimiter=delimiter
            )

            marker = response.get("NextMarker","")
            newFiles = [];
            for obj in response['Contents']:
                file = {};
                key = obj['Key']
                file['filename'] = os.path.basename(key);
                file['filepath'] = key;
                ext = os.path.splitext(key)[1][1:]
                # 文件扩展名
                if allowExts and ext not in allowExts:
                    continue;

                file['isdir'] = False;
                newFiles.append(file)

            return {"items":newFiles,"marker":marker};

        except Exception as e:
            self.uploadManager.setError(str(e))
            return False;

        return False;

    def deleteInternal(self, filepath, **options):

        try:
            client = self.getCosClient()
            bucket_name = options.get("bucket", self.bucket)
            response = client.delete_object(
                Bucket=bucket_name,
                Key=filepath
            )

            if response and isinstance(response, dict):
                return True

            return False

        except Exception as e:
            self.uploadManager.setError(str(e))
            return False;

        return False;


    def postInternal(self,file:dict,**options):

        import json,base64,datetime
        # 默认30 分钟过期
        expire = options.get('expire', 30);
        key = file['filepath'];
        endTime = datetime.datetime.now() + datetime.timedelta(minutes=expire)
        nowtime = int(time.time())
        qKeyTime = "{0};{1}".format(nowtime - 300, int(time.mktime(endTime.timetuple())))
        dir = os.path.dirname(key);

        policy = {
            "expiration":endTime.strftime("%Y-%m-%dT%H:%M:%S.000Z"),
            "conditions":[
                {"acl":"default"},
                {"bucket":self.bucket},
                ["starts-with","$key",dir],
                ["content-length-range", 0, 1048576000],
            ]
        };

        policyjsonstr = json.dumps(policy)
        response = {
            'action':self.buildDirecturl(),
            'key':key,
            'Signature':self.createSign(policyjsonstr,qKeyTime),
            'policy':bytes.decode(base64.b64encode(str.encode(policyjsonstr)))
        };

        return response;

    def buildDirecturl(self):

        if self.directurl:
            return self.directurl;

        directurl = 'http://{0}.cos.{1}.myqcloud.com/'.format(self.bucket,self.region);

        return directurl;


    def createSign(self,policyjsonstr,qKeyTime):

        import hashlib
        import hmac

        signKey = hmac.new(str.encode(self.secretKey), qKeyTime.encode("utf8"), hashlib.sha1).digest()
        sha = hashlib.sha1(policyjsonstr.encode("utf8"))
        stringToSign = sha.digest()
        qSignature = hmac.new(signKey, stringToSign, hashlib.sha1).hexdigest()

        return qSignature;












