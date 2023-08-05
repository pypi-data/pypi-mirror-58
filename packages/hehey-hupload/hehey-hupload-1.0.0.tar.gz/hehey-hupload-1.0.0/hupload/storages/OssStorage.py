
from ..upload import Storage
import os,time;
import oss2
from oss2.api import Bucket

"""
 * 阿里云oss存储器
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
class OssStorage(Storage):

    def __init__(self, **attrs):

        # oss accessId
        # <B> 说明： </B>
        # <pre>
        # 略
        # </pre>
        self.accessId = '';

        # oss secretKey
        # <B> 说明： </B>
        # <pre>
        # 略
        # </pre>
        self.secretKey = '';

        # 默认bucket
        # <B> 说明： </B>
        # <pre>
        # 略
        # </pre>
        self.bucket = '';

        # oss endpoint
        # <B> 说明： </B>
        # <pre>
        # 上传地址
        # </pre>
        self.endpoint = '';

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


    def getOssClient(self)->'Bucket':

        if self.ossClient:
            return self.ossClient

        auth = oss2.Auth(self.accessId, self.secretKey)
        self.ossClient = oss2.Bucket(auth, self.endpoint, self.bucket);

        return self.ossClient;

    def saveInternal(self,file,allowExts = [],**options):
        try :
            bucket = self.getOssClient()
            putObjectResult = bucket.put_object_from_file(file['filepath'], file['tmp_name'])
            if putObjectResult.status == 200:
                return file

        except Exception as e:
            self.uploadManager.setError(e.message);
            return False;

        return False;

    def filesInternal(self,dir,allowExts = [], **options):

        try :
            bucket = self.getOssClient()
            if dir[-1] != '/':
                prefix = dir + '/'
            else:
                prefix = dir;

            newFiles = [];
            for obj in oss2.ObjectIterator(bucket, prefix = prefix, delimiter='/'):
                file = {};
                file['filename'] = os.path.basename(obj.key);
                file['filepath'] = obj.key;
                # 通过is_prefix方法判断obj是否为文件夹。
                if obj.is_prefix():  # 文件夹
                    file['isdir'] = True;
                else:  # 文件
                    file['isdir'] = False;
                    ext = os.path.splitext(obj.key)[1][1:]
                    # 文件扩展名
                    if allowExts and ext not in allowExts:
                        continue;
                newFiles.append(file)

            return {"items":newFiles};

        except Exception as e:
            self.uploadManager.setError(str(e))
            return False;

        return False;

    def deleteInternal(self, filepath, **options):

        try:
            bucket = self.getOssClient()
            putObjectResult = bucket.delete_object(filepath)
            if putObjectResult.status != 0:
                return False
            else:
                return True

        except Exception as e:
            self.uploadManager.setError(str(e));
            return False;

        return False;


    def postInternal(self,file:dict,**options):

        import json;
        import base64
        import hashlib
        import hmac
        import datetime;

        filepath = file['filepath']
        expire = options.get('expire',30);
        endTime = datetime.datetime.now() + datetime.timedelta(minutes=expire)
        dir = os.path.dirname(filepath)
        condition = ("content-length-range", 0,1048576000);
        conditions = [condition];
        start = ("starts-with", filepath,dir)
        conditions.append(start)
        policyParams = {
            "expiration":oss2.date_to_iso8601(endTime),
            "conditions":conditions,
        };

        policy = json.dumps(policyParams)
        base64_policy = base64.b64encode(str.encode(policy))
        string_to_sign = base64_policy
        signing = hmac.new(str.encode(self.secretKey), string_to_sign, hashlib.sha1)
        signature = base64.b64encode(signing.digest())
        response = {
            "OSSAccessKeyId":self.accessId,
            'action':self.directurl,
            'policy':bytes.decode(base64_policy),
            'signature':bytes.decode(signature),
            'expire':int(time.mktime(endTime.timetuple())),
            'key':filepath,
        };

        return response;











