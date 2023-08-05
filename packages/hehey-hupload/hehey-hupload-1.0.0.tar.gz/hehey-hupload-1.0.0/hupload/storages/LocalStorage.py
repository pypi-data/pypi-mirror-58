
from ..upload import Storage
import os;
import shutil

"""
 * 本地存储器
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
class LocalStorage(Storage):

    def __init__(self, **attrs):

        # 上传根目录
        # <B> 说明： </B>
        # <pre>
        # 略
        # </pre>
        self.rootPath = '';

        super().__init__(**attrs)

        self.checkRootPath();

        return ;

    # 检测保存目录权限问题
    # <B> 说明： </B>
    # <pre>
    # 略
    # </pre>
    def checkSavePath(self,file):

        # 创建目录
        filepath = '{0}/{1}'.format(self.rootPath, file['filepath'])
        if not self.mkFileDir(filepath):
            return False;

        filedir = '{0}/{1}'.format(self.rootPath, os.path.dirname(file['filepath']))

        if not os.access(filedir, os.W_OK):
            return False;

        return True;

    # 检测根目录权限问题
    # <B> 说明： </B>
    # <pre>
    # 略
    # </pre>
    def checkRootPath(self):

        if not os.path.isdir(self.rootPath):
            os.makedirs(self.rootPath);

        return True;

    def buildFullFilepath(self,file):

        return '{0}/{1}'.format(self.rootPath, file['filepath'])

    def saveInternal(self,file,**options):

        if not self.checkSavePath(file):
            return False;

        fullFilepath = self.buildFullFilepath(file)

        # 移动,复制文件
        tmp_name = file['tmp_name'];
        shutil.move(tmp_name, fullFilepath)

        return file;


    def filesInternal(self,dir,allowExts = [], **options):

        return {"items": self.readfiles(dir,allowExts,**options)};

    def deleteInternal(self, filepath, **options):

        filepath = "{0}/{1}".format(self.rootPath, filepath)
        if os.path.exists(filepath):
            os.remove(filepath)

        return True;

    # 读取目录下所有文件
    # <B> 说明： </B>
    # <pre>
    # 略
    # </pre>
    def readfiles(self,dir,allowExts = [],**options):

        filedir = "{0}/{1}".format( self.rootPath ,dir)
        fileList = os.listdir(filedir)
        newFiles = [];
        # 输出所有文件和文件夹
        for filename in fileList:
            file = {};
            filepath = "{0}/{1}".format(dir,filename)
            file['filename'] = filename;
            file['filepath'] = filepath;
            if os.path.isdir(filepath):
                file['isdir'] = True;
            else:
                ext = os.path.splitext(filename)[1][1:]
                # 文件扩展名
                if allowExts and ext not in allowExts:
                    continue;
                file['isdir'] = False;

            newFiles.append(file);

        return newFiles;









