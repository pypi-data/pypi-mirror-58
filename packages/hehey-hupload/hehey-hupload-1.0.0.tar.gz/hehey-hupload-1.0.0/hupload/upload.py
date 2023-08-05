# -*- coding: utf-8 -*-

from .utils.UploadUtil import UploadUtil;

import os;
import time,hashlib

"""
 * 上传管理器
 *<B>说明：</B>
 *<pre>
 *  略
 *</pre>
 *<B>示例：</B>
 *<pre>
 * 
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
class UploadManager:


    def __init__(self,**attrs):

        # 默认存储器
        # <B> 说明： </B>
        # <pre>
        # 略
        # </pre>
        self.defaultStorage = '';

        # 定义存储器
        # <B> 说明： </B>
        # <pre>
        # 略
        # </pre>
        self.customStorages = {};

        # 存储器对象列表
        # <B> 说明： </B>
        # <pre>
        # 略
        # </pre>
        self.storages = {};

        # 错误消息模板
        # <B> 说明： </B>
        # <pre>
        # 略
        # </pre>
        self.errors = {

        }

        # 错误消息
        # <B> 说明： </B>
        # <pre>
        # 略
        # </pre>
        self.errmsg = '';



        if attrs:
            UploadUtil.setAttrs(self,attrs)

        return ;


    def makeStorage(self,storageType,options = {}):

        clazz = options.get('clazz', storageType)

        if not clazz:
            raise Exception('the {0} storage conf no find clazz'.format(storageType))

        if clazz.find('.') == -1:
            clazzName = UploadUtil.ucfirst(clazz) + 'Storage'
            clazz = __package__ + '.storages.' + clazzName + '.' + clazzName

        storageMeta = UploadUtil.getModuleMeta(clazz)
        uploadStorage = storageMeta(**options);
        uploadStorage.setUploadManager(self)

        return uploadStorage;


    def getStorage(self,storageType = '')->'Storage':

        if not storageType:
            storageType = self.defaultStorage;

        storage = self.storages.get(storageType, None)

        if storage:
            return storage

        storageConf = self.customStorages.get(storageType, None)
        if storageConf is None:
            raise Exception('the {0} storage conf no find'.format(storageType))

        storage = self.makeStorage(storageType, storageConf);
        self.storages[storageType] = storage

        return storage;

    # 上传文件
    # <B> 说明： </B>
    # <pre>
    # 略
    # </pre>
    def uploadFile(self,file,savePath = '',allowExts = [],**options):

        uploadStorage = self.getStorage();

        return uploadStorage.uploadFile(file,savePath,allowExts,**options);

    # 直传文件
    # <B> 说明： </B>
    # <pre>
    # 略
    # </pre>
    def directFile(self, filename = '', savePath='', allowExts=[], **options):

        uploadStorage = self.getStorage();

        return uploadStorage.directFile(filename, savePath, allowExts, **options);

    # 上次全部文件
    # <B> 说明： </B>
    # <pre>
    # 略
    # </pre>
    def uploadAll(self,files,savePath = '',allowExts = [],**options):

        uploadStorage = self.getStorage();

        return uploadStorage.uploadAll(files, savePath,allowExts, **options);

    def deleteFile(self, filepath,**options):

        uploadStorage = self.getStorage();

        return uploadStorage.deleteFile(filepath, **options);

    def setError(self,errmsg):

        self.errmsg = errmsg

        return ;

    def getError(self):

        return self.errmsg;

    def hasError(self):

        if self.errmsg:
            return True
        else:
            return False

    def clean(self):

        self.errmsg = '';

        return ;


    def formatMessage(self,key,params = {}):

        if not self.errors:
            self.errors = {
                "size":"上传文件大小不符,文件大小不允许超过{maxSize}",
                'ext':"上传文件后缀不允许,请上传带{exts}后缀文件",
                "mime":"上传文件MIME类型不允许,请上传以下{mimes}类型文件"
            };

        message = self.errors.get(key,"")

        if params:
            message = message.format(**params)

        return message;

    # 上传base64数据
    # <B> 说明： </B>
    # <pre>
    # 略
    # </pre>
    def uploadBase64(self, content, savePath='', allowExts=[], **options):

        uploadStorage = self.getStorage();

        return uploadStorage.uploadBase64(content, savePath, allowExts, **options);

    # 下载文件并上传
    # <B> 说明： </B>
    # <pre>
    # 略
    # </pre>
    def downloadAndUpload(self, url, savePath='', allowExts=[], **options):

        uploadStorage = self.getStorage();

        return uploadStorage.downloadAndUpload(url, savePath, allowExts, **options);


    def getFiles(self, dir = '',allowExts = [],**options):

        uploadStorage = self.getStorage();

        return uploadStorage.getFiles(dir,allowExts, **options);



    def buildBase64(self,filepath):


        return UploadUtil.buildBase64(filepath)


    def __getattr__(self, storageType):


        return self.getStorage(storageType)


class Storage:
    '''
        :type uploadManager: UploadManager
    '''
    def __init__(self, **attrs):

        # 允许上传的文件MiMe类型
        # <B> 说明： </B>
        # <pre>
        # 略
        # </pre>
        self.mimes = [];

        # 允许上传的文件后缀
        # <B> 说明： </B>
        # <pre>
        # 略
        # </pre>
        self.exts = [];

        # 允许上传的文件后缀
        # <B> 说明： </B>
        # <pre>
        # 上传的文件大小限制 (0-不做限制) b 单位
        # </pre>
        self.maxSize = 0;

        # 上传管理器
        # <B> 说明： </B>
        # <pre>
        # 略
        # </pre>
        self.uploadManager = None;


        if attrs:
            UploadUtil.setAttrs(self, attrs)

        return ;




    def setUploadManager(self,uploadManager):

        self.uploadManager = uploadManager

        return ;


    #  验证上传文件
    # <B> 说明： </B>
    # <pre>
    #   $file = array(
    #      "name" => pic1.gif,//文件名
    #      "type" => image/gif,//文件类型
    #      "size" => 59815,//文件大小
    #      "key" => name,//文件唯一key，一般用不到
    #      "isArray" =>false,是否数组中的上传文件
    #      "ext" => gif,//后缀
    #      "savename" => 52f8e85d0eaf8.gif,//新文件名
    #      "savepath" => 2014-02-10/,//保存目录
    #      "filepath" => 2014-02-10/52f8e85d0eaf8.gif,//文件相对路径
    #   );
    # </pre>
    def check(self,file:dict,allowExts = []):

        # 检测name
        fileKeys = file.keys()

        # 检测大小
        if "size" in fileKeys and not self.checkSize(file['size']):
            self.uploadManager.setError(self.formatMessage("size"),{"maxSize":self.formatSize(self.maxSize)})
            return False;

        # 检测Mime类型
        if "type" in fileKeys and not self.checkMime(file['type']):
            self.uploadManager.setError(self.formatMessage("mime"), {"mimes": ",".join(self.mimes)})
            return False;

        # 检测文件扩展名
        if "ext" in fileKeys and not self.checkExt(file['ext'],allowExts):
            self.uploadManager.setError(self.formatMessage("ext"), {"exts": ",".join(self.exts)})
            return False;

        return True;

    # 检测文件大小
    # <B> 说明： </B>
    # <pre>
    # 略
    # </pre>
    def checkSize(self,size = 0):

        if self.maxSize == 0 or size <= self.maxSize:
            return True
        else:
            return False;

    #  检查上传的文件MIME类型是否合法
    # <B> 说明： </B>
    # <pre>
    # 略
    # </pre>
    def checkMime(self,mime:str):

        if len(self.mimes) > 0:
            if mime.lower() in self.mimes:
                return True;
            else:
                return False;
        else:
            return True;

    # 检查上传的文件后缀是否合法
    # <B> 说明： </B>
    # <pre>
    # 略
    # </pre>
    def checkExt(self,ext,allowExts = []):

        if len(allowExts) > 0:
            if ext.lower() in allowExts:
                return True;
            else:
                return False;

        if len(self.exts) > 0:
            if ext.lower() in self.exts:
                return True;
            else:
                return False;
        else:
            return True;

    # 解析文件最大大小
    # <B> 说明： </B>
    # <pre>
    # 解析成“2.5MB”格式
    # </pre>
    def formatSize(self,filesize):

        if filesize >= 1073741824:
            filesizeText =  '{0}Gb'.format(round(filesize/1073741824 * 100) / 100)
        elif filesize >= 1048576:
            filesizeText = '{0}MB'.format(round(filesize/1048576 * 100))
        elif filesize >= 1024:
            filesizeText = '{0}KB'.format(round(filesize/1024 * 100) / 100)
        else:
            filesizeText = '{0}B'.format(filesize)

        return filesizeText;

    # 创建文件目录
    # <B> 说明： </B>
    # <pre>
    # 略
    # </pre>
    def mkFileDir(self,filepath):

        filedir =  os.path.dirname(filepath)
        if os.path.exists(filedir):
            return True;

        os.makedirs(filedir);

        return True;


    def formatFile(self,file:dict):

        # 扩展名
        file['ext'] = self.getFileExt(file);

        # 定义保存新文件名
        savepath = file.get("savepath", None)
        if savepath is None:
            file['savepath'] = self.buildSavepath()
        else:
            filename = os.path.basename(savepath)
            if filename:
                file['savename'] = filename;

        # 定义保存新文件名
        savename = file.get("savename",None)
        if savename is None:
            file['savename'] = self.buildFilename(file)

        # 定义保存新文件名
        filepath = file.get("filepath", None)
        if filepath is None:
            file['filepath'] = '{0}/{1}'.format(file['savepath'],file['savename'])
        else:
            file['savepath'] = os.path.dirname(file['filepath'])
            file['savename'] = os.path.basename(file['filepath'])

        return file;

    # 构建随机文件名
    # <B> 说明： </B>
    # <pre>
    # 不带扩展名
    # </pre>
    def buildRandFilename(self):

        m = hashlib.md5()
        m.update(bytes(str(time.clock()), encoding='utf-8'))

        return m.hexdigest()

    # 构建保存目录
    # <B> 说明： </B>
    # <pre>
    # 略
    # </pre>
    def buildSavepath(self):

        return time.strftime('%Y/%m/%d',time.localtime(time.time()));

    # 重新构建文件名
    # <B> 说明： </B>
    # <pre>
    # 略
    # </pre>
    def buildFilename(self,file):

        return "{0}.{1}".format(self.buildRandFilename(),self.getFileExt(file))

    # 构建base64 文件
    # <B> 说明： </B>
    # <pre>
    # 略
    # </pre>
    def buildBase64File(self,content:str):

        import base64
        base64Data = content.split(',')

        # 读取后缀
        extStr = base64Data[0].split(";");
        extStr = extStr[0].split(":")
        extArr = extStr[1].split("/")
        ext = '';
        if len(extArr) == 2:
            ext = extArr[1]

        fileContent = base64.b64decode(base64Data[1]);
        tempFile = self.createTmpfile(ext);
        with open(tempFile,'wb') as f:
            f.write(fileContent)


        return self.buildUploadFile(tempFile);

    # 获取文件扩展名
    # <B> 说明： </B>
    # <pre>
    # 略
    # </pre>
    def getFileExt(self,file:dict):

        fileExt = file.get("ext",None)
        if fileExt:
            return fileExt;

        savename = file.get("savename",None)
        if savename:
            return  os.path.splitext(savename)[1][1:]

        filepath = file.get("filepath", None)
        if filepath:
            return os.path.splitext(filepath)[1][1:]

        filename = file.get("name", None)
        if filename:
            return os.path.splitext(filename)[1][1:]

        tmp_name = file.get("tmp_name", None)
        if tmp_name:
            return UploadUtil.getFileExtension(file['tmp_name'])

        return "";

    # 创建临时文件名称
    # <B> 说明： </B>
    # <pre>
    # 略
    # </pre>
    def createTmpfile(self,ext = '',path = ''):

        import tempfile

        if not path:
            path = tempfile.gettempdir()

        if ext:
            filename = "{0}.{1}".format(self.buildRandFilename(), ext)
        else:
            filename = self.buildRandFilename()

        filepath = '{0}/{1}/{2}'.format(path, self.buildSavepath(), filename)

        self.mkFileDir(filepath)

        return filepath;

    # 上传整个文件组
    # <B> 说明： </B>
    # <pre>
    # 略
    # </pre>
    def uploadAll(self,files,savePath = '',allowExts = [],**options):

        newFiles = [];
        for i in range(len(files)):
            result = self.uploadFile(files[i],savePath,allowExts,**options)
            newFiles.append(result);

        return newFiles;

    # 批量上传多个文件
    # <B> 说明： </B>
    # <pre>
    # 一般用于上传图片组
    # </pre>
    def batchUpload(self,files,savePath = ''):

        return ;

    # 上传单个文件
    # <B> 说明： </B>
    # <pre>
    # 略
    # </pre>
    def uploadFile(self,file,savePath = '',allowExts = [],**options):

        uploadFile = self.buildUploadFile(file);

        if savePath:
            uploadFile['savepath'] = savePath
            filename = os.path.basename(savePath);

        uploadFile = self.formatFile(uploadFile);

        if not self.check(uploadFile,allowExts):
            return False;
        uploadResult = self.saveInternal(uploadFile,**options);

        return uploadResult;


    # 直传单个文件
    # <B> 说明： </B>
    # <pre>
    # 略
    # </pre>
    def directFile(self, filename, savePath='', allowExts=[], **options):

        uploadFile = self.buildUploadFile(filename);

        if savePath:
            uploadFile['savepath'] = savePath

        uploadFile = self.formatFile(uploadFile);

        if not self.check(uploadFile, allowExts):
            return False;

        uploadResult = self.postInternal(uploadFile, **options);

        return uploadResult;

    # 上传base64数据
    # <B> 说明： </B>
    # <pre>
    # 略
    # </pre>
    def uploadBase64(self,content,savePath='', allowExts=[], **options):

        file = self.buildBase64File(content);

        return self.uploadFile(file,savePath,allowExts,**options);

    # 下载文件
    # <B> 说明： </B>
    # <pre>
    # 略
    # </pre>
    def downloadFile(self,url):

        import urllib;
        filename = os.path.basename(url)
        fileext = os.path.splitext(filename)[1][1:]
        if fileext:
            tmpfile = self.createTmpfile(fileext)
        else:
            tmpfile = self.createTmpfile()
        urllib.request.urlretrieve(url, tmpfile)

        return tmpfile;


    # 下载问加你并上传
    # <B> 说明： </B>
    # <pre>
    # 略
    # </pre>
    def downloadAndUpload(self, url, savePath = '', allowExts=[], **options):

        file = self.downloadFile(url)

        return self.uploadFile(file, savePath, allowExts, **options);

    def buildUploadFile(self,filepath):

        if isinstance(filepath,str):
            return {"tmp_name":filepath,"name":os.path.basename(filepath)};
        else:
            return filepath

    # 删除文件
    # <B> 说明： </B>
    # <pre>
    # 略
    # </pre>
    def deleteFile(self,filepath,**options):

        return self.deleteInternal(filepath,**options);

    # 上传单个文件
    # <B> 说明： </B>
    # <pre>
    # 略
    # </pre>
    def getFiles(self,dir = '',allowExts = [],**options):

        return self.filesInternal(dir,allowExts,**options);

    # 保存文件入口
    # <B> 说明： </B>
    # <pre>
    # 略
    # </pre>
    def saveInternal(self,file:dict,**options):

        return ;

    # 获取文件入口
    # <B> 说明： </B>
    # <pre>
    # 略
    # </pre>
    def filesInternal(self,dir,allowExts = [], **options):

        return;

    # 删除文件入口
    # <B> 说明： </B>
    # <pre>
    # 略
    # </pre>
    def deleteInternal(self, filepath,**options):

        return;

    # 直传入口
    # <B> 说明： </B>
    # <pre>
    # 略
    # </pre>
    def postInternal(self,file:dict,**options):


        return ;



    # https://blog.csdn.net/yagerfgcs/article/details/51427085










