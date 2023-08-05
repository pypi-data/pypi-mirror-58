# -*- coding: utf-8 -*-
# Create your views here.

from __future__ import unicode_literals
from rest_framework import viewsets
from rest_framework.response import Response
from django.http import FileResponse
from django.utils.decorators import method_decorator
from .errorList import generateError
from .thstorage import THSClient,loginAuth
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

import datetime, json, uuid, time
import sys, os, shutil, hashlib
import requests
from .models import *

#reload(sys)
#sys.setdefaultencoding('utf-8')

config = {
    'server': settings.TH_STORAGE_CONFIG.get("STORAGE_BACKEND_HOST",''),
    'appid': settings.TH_STORAGE_CONFIG.get('STORAGE_BACKEND_APPID',''),
    'appkey': settings.TH_STORAGE_CONFIG.get('STORAGE_BACKEND_APPKEY',''),
}


def formatDate(date):
    dateString = date.split('+')[0].split('.')[0].replace('T', ' ').replace('Z', '')
    dateTime = datetime.datetime.strptime(dateString, '%Y-%m-%d %H:%M:%S')
    return dateTime


def CheckKeys(inputData, keyList=[]):
    '''
    检查inputData中是否包含keyList中的所有的key，如缺少某个key，报错缺少key。
    '''
    for key in keyList:
        if key not in inputData.keys():
            return {"status": 1, "lackKey": key}
    return {"status": 0}


def GenerateToken():
    '''
    生成一个32位的随机令牌
    '''
    random_str = str(uuid.uuid1())
    m = hashlib.md5()
    m.update(random_str)
    token = m.hexdigest().decode('utf-8')
    return token


def GenerateFailedResponse(errorInfo):
    '''
    根据错误码和错误描述，生成一个失败的消息。
    '''
    errorCode = errorInfo[0]
    errorDesc = errorInfo[1]
    print
    errorCode, errorDesc
    return Response({"success": "no",
                     "error_code": errorCode,
                     "error_desc": errorDesc})


def GenerateFailedResponse2(errorInfo):
    '''
    根据错误码和错误描述，生成一个失败的消息。
    '''
    errorCode = errorInfo['error_code']
    errorDesc = errorInfo['error_desc']
    return Response({"success": "no",
                     "error_code": errorCode,
                     "error_desc": errorDesc})


class AddUser(viewsets.ViewSet):
    def create(self, request):
        inputData = request.data
        keyList = ['platform', 'username', 'password', 'totalCapacity']
        checkKeys = CheckKeys(inputData, keyList)
        if not checkKeys['status'] == 0:
            lackKey = checkKeys['lackKey']
            return GenerateFailedResponse(generateError('paramLack', lackKey))
        platform = inputData['platform']
        username = inputData['username']
        password = inputData['password']
        totalCapacity = inputData['totalCapacity']
        if 'tokenValidityPeriod' in inputData.keys():
            tokenValidityPeriod = inputData['tokenValidityPeriod']
        else:
            tokenValidityPeriod = 36000000
        usedCapacity = 0
        if models.NetDiskUser.objects.filter(platform=platform, username=username):
            return GenerateFailedResponse(generateError('usernameExist', username))
        models.NetDiskUser.objects.create(platform=platform,
                                          username=username,
                                          password=password,
                                          tokenValidityPeriod=tokenValidityPeriod,
                                          totalCapacity=totalCapacity,
                                          usedCapacity=usedCapacity)
        return Response({"success": "yes"})


class UpdateQuota(viewsets.ViewSet):
    def create(self, request):
        '''
        更新所有在7天内登录过的用户的空间使用信息
        '''
        users = models.NetDiskUser.objects.all()
        for userInfo in users:
            if userInfo.tokenGererateTime:
                timeNow = time.time()
                if (timeNow - float(userInfo.tokenGererateTime)) <= 604800:
                    id = userInfo.id
                    homePath = config['homePath']
                    userHomePath = os.path.join(homePath, userInfo.username, 'files')
                    try:
                        # du_command = "du -sb %s | awk '{ print $1 }'" % userHomePath
                        du_command = "diskus %s | awk -F\( '{ print $2 }' | awk '{ print $1 }'" % userHomePath
                        result = os.popen(du_command).read()
                        newUsedCapacity = int(result[0:len(result) - 1])
                    except:
                        return GenerateFailedResponse(generateError('duFailed'))
                    models.NetDiskUser.objects.filter(id=id).update(usedCapacity=newUsedCapacity)
        return Response({"success": "yes"})


class UserLogin(viewsets.ViewSet):
    def create(self, request):
        '''
        验证用户登录请求是否合法，合法时返回token给用户
        '''
        inputData = request.data
        keyList = ['username', 'password']
        checkKeys = CheckKeys(inputData, keyList)
        if not checkKeys['status'] == 0:
            lackKey = checkKeys['lackKey']
            return GenerateFailedResponse(generateError('paramLack', lackKey))
        # platform = inputData['platform']
        username = inputData.get('username')
        password = inputData.get('password')
        ##调用单点登录接口
        post_data = {"username": username, "password": password}
        url = "http://50.50.50.12:8000/third_platform_login/"
        req = requests.post(url, data=post_data)
        body = json.loads(req.text)
        # 临时更改位置1，共5
        if '1' == '1':
            # if body['success'] == 'yes':
            # 临时更改位置2，共5
            if '1' == '1':
                # if body['userinfo']['status'] == 'actived':
                appid = 'test'
                appkey = '1523333014.414702'
                timeNow = time.time()
                combStr = appkey + str(timeNow)
                hl = hashlib.md5()
                hl.update(combStr.encode(encoding='utf-8'))
                sid = hl.hexdigest()
                storageUrl = "http://172.18.1.171:5000/users/%s?appid=%s&sid=%s&timestamp=%s" % (
                username, appid, sid, timeNow)
                storageReq = requests.get(storageUrl)
                print
                storageReq
                print
                storageReq.text
                storageBody = json.loads(storageReq.text)
                # 临时更改位置3，共5
                if '1' == '1':
                    # if storageBody['success'] == 'yes':
                    # 临时更改位置3，共4
                    quota = 100 * 1000000000
                    # quota = storageBody['userinfo']['quota'] * 1000000000
                    token = GenerateToken()
                    nowTime = int(time.time())
                    if not models.NetDiskUser.objects.filter(username=username):
                        homePath = config['homePath']
                        userHomePath = os.path.join(homePath, username, 'files')
                        try:
                            du_command = "du -sb %s | awk '{ print $1 }'" % userHomePath
                            result = os.popen(du_command).read()
                            usedCapacity = int(result[0:len(result) - 1])
                        except:
                            return GenerateFailedResponse(generateError('duFailed'))
                        models.NetDiskUser.objects.create(platform='test',
                                                          username=username,
                                                          password='-',
                                                          tokenValidityPeriod=36000000,
                                                          totalCapacity=quota,
                                                          usedCapacity=usedCapacity,
                                                          token=token,
                                                          tokenGererateTime=nowTime, )
                    else:  # if not models.NetDiskUser.objects.filter(username=username):
                        models.NetDiskUser.objects.filter(username=username).update(totalCapacity=quota, token=token,
                                                                                    tokenGererateTime=nowTime)
                    homePath = config['homePath']
                    workPath = os.path.join(homePath, username, 'files')
                    mkdir_command = "mkdir -p %s" % workPath
                    try:
                        if not os.path.exists(workPath):
                            result = os.system(mkdir_command)
                            if not result == 0:
                                return GenerateFailedResponse(generateError('mkdirFailed'))
                            # 将该目录的属主改为apache
                            chown_command = "chown %s:%s %s" % ('apache', 'apache', workPath)
                            try:
                                result = os.system(chown_command)
                                if not result == 0:
                                    return GenerateFailedResponse(generateError('chownFailed'))
                            except:
                                return GenerateFailedResponse(generateError('chownFailed'))
                    except Exception:
                        return GenerateFailedResponse(generateError('mkdirFailed'))

                    print
                    "login success."
                    return Response({"success": "yes", "token": token})
                else:  # if storageBody['success'] == 'yes':
                    return GenerateFailedResponse2(storageBody)
            else:  # body['userinfo']['status'] == 'actived':
                return GenerateFailedResponse(generateError('UserNotActive'))
        else:
            return GenerateFailedResponse2(body)


class ContentList(viewsets.ViewSet):
    @method_decorator(loginAuth)
    def create(self, request):
        '''
        获取用户某个目录下的所有文件和目录的列表信息。
        '''
        inputData = request.data
        keyList = ['platform', 'username', 'encrypedToken', 'timestamp', 'path']
        checkKeys = CheckKeys(inputData, keyList)
        print(inputData)
        if not checkKeys['status'] == 0:
            lackKey = checkKeys['lackKey']
            return GenerateFailedResponse(generateError('paramLack', lackKey))
        path = inputData['path']
        cluster = inputData.get("cluster")
        user = inputData.get("username")
        ################   ↑↑↑↑↑↑   以上常规检查工作结束   ↑↑↑↑↑↑   ###################
        # 获取可选参数
        if 'keyword' in inputData.keys() and inputData['keyword']:
            keyword = inputData['keyword']
        else:
            keyword = ''
        if 'sort' in inputData.keys() and inputData['sort']:
            sort = inputData['sort']
        else:
            sort = ''
        if 'sortDirection' in inputData.keys() and inputData['sortDirection'] == u'desc':
            desc = 1
        else:
            desc = 0
        # 通过SDK，访问资源层接口
        client = THSClient(config['appid'], config['appkey'], config['server'], cluster, user, path)
        try:
            objs = client.listObjects(sort=sort, desc=desc, page=1, count=0, search=keyword)
            if objs:
                return Response({"success": "yes",
                                 "listLength": len(objs['objects']),
                                 "listContent": objs['objects']})
            else:
                return Response({"success": "yes",
                                 "listLength": 0,
                                 "listContent": []})
        except Exception as e:
            print
            e
            return Response({"success": "no", "error_desc": eval(str(e))['Message']})


class Capacity(viewsets.ViewSet):
    @method_decorator(loginAuth)
    def create(self, request):
        '''
        查询用户当前的总空间和已使用空间
        '''
        inputData = request.data
        keyList = ['platform', 'username', 'encrypedToken', 'timestamp', ]
        checkKeys = CheckKeys(inputData, keyList)
        if not checkKeys['status'] == 0:
            lackKey = checkKeys['lackKey']
            return GenerateFailedResponse(generateError('paramLack', lackKey))
        platform = inputData.get('platform')
        user = inputData.get('username')
        cluster = inputData.get("cluster")

        totalCapacity = 10000000
        usedCapacity = 1002334

        capacity = {}
        capacity['username'] = user
        capacity['totalCapacity'] = totalCapacity
        capacity['usedCapacity'] = usedCapacity

        return Response({"success": "yes", "capacity": capacity})


class NewFile(viewsets.ViewSet):
    @method_decorator(loginAuth)
    def create(self, request):
        '''
        在服务器上创建一个新的空文件
        '''
        inputData = request.data
        keyList = ['platform', 'username', 'encrypedToken', 'timestamp', 'serverPath', 'fileName']
        checkKeys = CheckKeys(inputData, keyList)
        if not checkKeys['status'] == 0:
            lackKey = checkKeys['lackKey']
            return GenerateFailedResponse(generateError('paramLack', lackKey))
        serverPath = inputData['serverPath'].replace('\\', '/')
        fileName = inputData['fileName']
        ################   ↑↑↑↑↑↑   以上常规检查工作结束   ↑↑↑↑↑↑   ###################
        # 获取可选参数
        user = inputData.get("username")
        cluster = inputData.get("cluster")
        dir = 0
        path = os.path.join(serverPath, fileName)

        # 通过SDK，访问资源层接口
        client = THSClient(config['appid'], config['appkey'], config['server'], cluster, user, path)
        try:
            objs = client.createObject(dir=dir)
            return Response({"success": "yes"})
        except Exception as e:
            print
            e
            print
            type(e)
            return Response({"success": "no",
                             "error_desc": eval(str(e))['Message']})


class NewFolder(viewsets.ViewSet):
    @method_decorator(loginAuth)
    def create(self, request):
        '''
        在服务器上创建一个新的目录
        '''
        inputData = request.data
        keyList = ['platform', 'username', 'encrypedToken', 'timestamp', 'path']
        checkKeys = CheckKeys(inputData, keyList)
        if not checkKeys['status'] == 0:
            lackKey = checkKeys['lackKey']
            return GenerateFailedResponse(generateError('paramLack', lackKey))

        path = inputData['path']
        ################   ↑↑↑↑↑↑   以上常规检查工作结束   ↑↑↑↑↑↑   ###################
        # 获取可选参数
        user = inputData.get("username")
        cluster = inputData.get("cluster")
        dir = 1

        # 通过SDK，访问资源层接口
        client = THSClient(config['appid'], config['appkey'], config['server'], cluster, user, path)
        try:
            objs = client.createObject(dir=dir)
            return Response({"success": "yes"})
        except Exception as e:
            print
            eval(str(e))
            return Response({"success": "no",
                             "error_desc": eval(str(e))['Message']})


class Delete(viewsets.ViewSet):
    @method_decorator(loginAuth)
    def create(self, request):
        '''
        在服务器上删除一个目录或文件
        '''
        inputData = request.data
        keyList = ['platform', 'username', 'encrypedToken', 'timestamp', 'serverPathList']
        checkKeys = CheckKeys(inputData, keyList)
        if not checkKeys['status'] == 0:
            lackKey = checkKeys['lackKey']
            return GenerateFailedResponse(generateError('paramLack', lackKey))
        serverPathList = inputData['serverPathList']
        # totalCapacity = models.NetDiskUser.objects.filter(platform=platform, username=username)[0].totalCapacity
        # usedCapacity = models.NetDiskUser.objects.filter(platform=platform, username=username)[0].usedCapacity
        ################   ↑↑↑↑↑↑   以上常规检查工作结束   ↑↑↑↑↑↑   ###################
        # 获取可选参数
        user = inputData.get('username')
        cluster = inputData.get('cluster')

        # 通过SDK，访问资源层接口
        try:
            for path in serverPathList.strip(',').split(','):
                client = THSClient(config['appid'], config['appkey'], config['server'], cluster, user, path)
                objs = client.deleteObject(recursive=1)
            return Response({"success": "yes"})
        except Exception as e:
            print
            e
            return Response({"success": "no",
                             "error_desc": eval(str(e))['Message']})


class CopyTo(viewsets.ViewSet):
    @method_decorator(loginAuth)
    def create(self, request):
        '''
        在服务器上复制一个或多个目录或文件。
        '''
        inputData = request.data
        keyList = ['platform', 'username', 'encrypedToken', 'timestamp', 'oldPathList', 'newPath']
        checkKeys = CheckKeys(inputData, keyList)
        if not checkKeys['status'] == 0:
            lackKey = checkKeys['lackKey']
            return GenerateFailedResponse(generateError('paramLack', lackKey))
        oldPathList = inputData['oldPathList']
        newPath = inputData['newPath']
        ################   ↑↑↑↑↑↑   以上常规检查工作结束   ↑↑↑↑↑↑   ###################
        for sourcePath in oldPathList.strip(',').split(','):
            if newPath.startswith(sourcePath):
                return Response({"success": "no", "error_desc": "目的地址不能是源地址的子目录"})
        # 获取可选参数
        user = inputData.get("username")
        cluster = inputData.get("cluster")
        # path = newPath

        failedList = []
        failedInfo = {}

        # 通过SDK，访问资源层接口
        # client = THSClient(config['appid'], config['appkey'], config['server'], cluster, user, path)
        for sourcePath in oldPathList.strip(',').split(','):
            try:
                path = os.path.join(newPath, os.path.basename(sourcePath))
                client = THSClient(config['appid'], config['appkey'], config['server'], cluster, user, path)
                objs = client.copyObject(sourcePath, recursive=1)
            except Exception as e:
                print
                eval(str(e))['Code']
                failedInfo['name'] = os.path.basename(sourcePath)
                failedInfo['reason'] = eval(str(e))['Code']
                failedList.append(failedInfo.copy())

        return Response({"success": "yes",
                         "failedList": failedList})


class CutTo(viewsets.ViewSet):
    @method_decorator(loginAuth)
    def create(self, request):
        '''
        在服务器上移动一个或多个目录或文件。
        '''
        # inputData = json.loads(request.data.keys()[0])
        inputData = request.data
        keyList = ['platform', 'username', 'encrypedToken', 'timestamp', 'oldPathList', 'newPath']
        checkKeys = CheckKeys(inputData, keyList)
        if not checkKeys['status'] == 0:
            lackKey = checkKeys['lackKey']
            return GenerateFailedResponse(generateError('paramLack', lackKey))
        oldPathList = inputData['oldPathList']
        newPath = inputData['newPath']
        ################   ↑↑↑↑↑↑   以上常规检查工作结束   ↑↑↑↑↑↑   ###################
        for sourcePath in oldPathList.strip(',').split(','):
            if newPath.startswith(sourcePath):
                return Response({"success": "no", "error_desc": "目的地址不能是源地址的子目录"})
        # 获取可选参数
        user = inputData.get("username")
        cluster = inputData.get("cluster")
        # path = newPath

        failedList = []
        failedInfo = {}

        # 通过SDK，访问资源层接口
        # client = THSClient(config['appid'], config['appkey'], config['server'], cluster, user, path)
        for sourcePath in oldPathList.strip(',').split(','):
            try:
                path = os.path.join(newPath, os.path.basename(sourcePath))
                client = THSClient(config['appid'], config['appkey'], config['server'], cluster, user, path)
                # print sourcePath, path
                objs = client.moveObject(sourcePath, recursive=1)
            except Exception as e:
                failedInfo['name'] = os.path.basename(sourcePath)
                failedInfo['reason'] = eval(str(e))['Code']
                failedList.append(failedInfo.copy())

        return Response({"success": "yes",
                         "failedList": failedList})


class Rename(viewsets.ViewSet):
    def create(self, request):
        '''
        在服务器上重命名一个或多个目录或文件。
        '''
        # inputData = json.loads(request.data.keys()[0])
        inputData = request.data
        keyList = ['platform', 'username', 'encrypedToken', 'timestamp', 'path', 'oldName', 'newName']
        checkKeys = CheckKeys(inputData, keyList)
        if not checkKeys['status'] == 0:
            lackKey = checkKeys['lackKey']
            return GenerateFailedResponse(generateError('paramLack', lackKey))
        path = inputData['path']
        oldName = inputData['oldName']
        newName = inputData['newName']
        ################   ↑↑↑↑↑↑   以上常规检查工作结束   ↑↑↑↑↑↑   ###################
        # 获取可选参数
        user = inputData.get("username")
        cluster = inputData.get("cluster")
        oldPath = os.path.join(path, oldName.strip('/'))
        newPath = os.path.join(path, newName.strip('/'))

        # 通过SDK，访问资源层接口
        client = THSClient(config['appid'], config['appkey'], config['server'], cluster, user, newPath)
        try:
            # print oldPath, newPath
            objs = client.moveObject(oldPath, recursive=1)
            return Response({"success": "yes"})
        except Exception as e:
            print
            e
            # return Response({"success":"no",
            #                "error_desc":eval(str(e))['Code']})
            return Response({"success": "no",
                             "error_desc": eval(str(e))['Message']})


class Attribute(viewsets.ViewSet):
    @method_decorator(loginAuth)
    def create(self, request):
        '''
        获取某个文件或目录的属性信息。
        '''
        # inputData = json.loads(request.data.keys()[0])
        inputData = request.data
        keyList = ['platform', 'username', 'encrypedToken', 'timestamp', 'path']
        checkKeys = CheckKeys(inputData, keyList)
        if not checkKeys['status'] == 0:
            lackKey = checkKeys['lackKey']
            return GenerateFailedResponse(generateError('paramLack', lackKey))
        path = inputData['path']
        ################   ↑↑↑↑↑↑   以上常规检查工作结束   ↑↑↑↑↑↑   ###################
        # 获取可选参数
        user = inputData.get("username")
        cluster = inputData.get("cluster")

        # 通过SDK，访问资源层接口
        client = THSClient(config['appid'], config['appkey'], config['server'], cluster, user, path)
        try:
            objs = client.getObjectMeta()
            print
            objs
            return Response({"success": "yes", "attribute": objs})
        except Exception as e:
            print
            e
            return Response({"success": "no",
                             "error_desc": eval(str(e))['Message']})

class webUploadFile(viewsets.ViewSet):
    @method_decorator(loginAuth)
    def create(self, request):
        inputData = request.data
        print(inputData)
        keyList = ['platform', 'username', 'encrypedToken', 'timestamp', 'serverPath', 'file']
        checkKeys = CheckKeys(inputData, keyList)
        if not checkKeys['status'] == 0:
            lackKey = checkKeys['lackKey']
            return Response({"error": 'paramLack'}, status=400)
            # return GenerateFailedResponse(generateError('paramLack', lackKey))
        fileData = inputData['file']
        ################   ↑↑↑↑↑↑   以上常规检查工作结束   ↑↑↑↑↑↑   ###################
        fileName = inputData['filename']
        # tmpFileName = fileName + '.thgyy.uploading'
        tmpFileName = fileName
        serverPath = inputData['serverPath'].replace('\\', '/')
        if serverPath == '/':
            destPath = os.path.join(serverPath, tmpFileName)
        else:
            destPath = os.path.join(serverPath.rstrip('/'), tmpFileName)

        chunkNumber = int(inputData['chunkNumber'])
        totalChunks = int(inputData['totalChunks'])
        totalSize = int(inputData['totalSize'])
        user = inputData.get('username')
        cluster = inputData.get('cluster')

        # 如果上传的是空文件，调用createObject接口
        if totalSize == 0:
            dir = 0
            path = os.path.join(serverPath, tmpFileName)
            # 通过SDK，访问资源层接口
            client = THSClient(config['appid'], config['appkey'], config['server'], cluster, user, path)
            try:
                objs = client.createObject(dir=dir)
                return Response({"success": "yes"})
            except Exception as e:
                return Response({"error": eval(str(e))['Code']}, status=400)
                # return Response({"success":"no",
                #                "error_desc":eval(str(e))['Message']})

        # 通过SDK，访问资源层接口
        client = THSClient(config['appid'], config['appkey'], config['server'], cluster, user, destPath)
        if chunkNumber == 1:
            first = True
            for chunk in fileData.chunks():
                if first:
                    try:
                        print
                        "1111111111111111111111111111111111111111111111111111111111111111"
                        objs = client.putObject(file=chunk)
                        first = False
                    except Exception as e:
                        print
                        "1", e
                        return Response({"error": eval(str(e))['Code']}, status=400)
                        # return Response({"success":"no",
                        #                "error_desc":eval(str(e))['Message']})
                else:
                    try:
                        print
                        "2222222222222222222222222222222222222222222222222222222222222222"
                        objs = client.appendObject(file=chunk)
                    except Exception as e:
                        print
                        "2", e
                        return Response({"error": eval(str(e))['Code']}, status=400)
                        # return Response({"success":"no",
                        #                "error_desc":eval(str(e))['Message']})
        else:
            for chunk in fileData.chunks():
                try:
                    print
                    "33333333333333333333333333333333333333333333333333333333333333333333"
                    print
                    "chunkNumber=", chunkNumber
                    objs = client.appendObject(file=chunk)
                except Exception as e:
                    print
                    "3", e
                    return Response({"error": eval(str(e))['Code']}, status=400)
                    # return Response({"success":"no",
                    #                "error_desc":eval(str(e))['Message']})

        #
        # if chunkNumber == totalChunks:
        #    if serverPath == '/':
        #        newDestPath = os.path.join(serverPath, fileName)
        #    else:
        #        newDestPath = os.path.join(serverPath.rstrip('/'), fileName)
        #    # 通过SDK，访问资源层接口
        #    client = THSClient(config['appid'], config['appkey'], config['server'], cluster, user, newDestPath)
        #    try:
        #        objs = client.moveObject(destPath, recursive=1)
        #    except Exception as e:
        #        print eval(str(e))['Code']
        #        return Response({"error":eval(str(e))['Message']}, status=400)
        # if eval(str(e))['Code'] == 'ObjectNameExists':
        #    nowTime = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
        #    newDestPath = newDestPath + "." + nowTime
        #    client = THSClient(config['appid'], config['appkey'], config['server'], cluster, user, newDestPath)
        #    try:
        #        objs = client.moveObject(destPath, recursive=1)
        #    except Exception as e:
        #        return Response({"success":"no",
        #                        "error_desc":eval(str(e))['Message']})

        return Response({"success": "yes"})


class DownloadFile(viewsets.ViewSet):
    def create(self, request):
        '''
        获取某个文件或目录的属性信息。
        '''
        inputData = request.data
        keyList = ['platform', 'username', 'encrypedToken', 'timestamp', 'serverPath', 'startData', 'endData']
        checkKeys = CheckKeys(inputData, keyList)
        if not checkKeys['status'] == 0:
            lackKey = checkKeys['lackKey']
            return GenerateFailedResponse(generateError('paramLack', lackKey))
        username = inputData['username']
        ################   ↑↑↑↑↑↑   以上常规检查工作结束   ↑↑↑↑↑↑   ###################
        serverPath = inputData['serverPath'].replace('\\', '/')
        fileName = os.path.basename(serverPath)
        tmpFileName = fileName + '.thgyy.downloading'
        startData = int(inputData['startData'])
        endData = int(inputData['endData'])
        sourcePath = os.path.join(config['homePath'], username, 'files', serverPath.strip('/'))
        if not os.path.exists(sourcePath):
            return GenerateFailedResponse(generateError('sourcePathNotExist'))
        if (os.path.isdir(sourcePath)):
            return GenerateFailedResponse(generateError('sourcePathIsDir'))

        # openMode = 'rb'
        def file_iterator(sourcePath, chunk_size=4):
            with open(sourcePath, 'rb') as f:
                f.seek(startData)
                c = f.read(endData - startData)
                yield c

        response = FileResponse(file_iterator(sourcePath))
        response['content-type'] = 'application/octet-stream'
        # response['Content-Disposition'] = 'attachment;filename="{0}"'.format(fileName.encode('gbk'))
        response['content-length'] = os.path.getsize(sourcePath)  # 传输给客户端的文件大小
        if 'requestMd5' in inputData.keys() and inputData['requestMd5']:
            with open(sourcePath, 'rb') as ft:
                filemd5 = hashlib.md5()
                filemd5.update(ft.read())
                filemd5 = filemd5.hexdigest()
                response['filemd5'] = filemd5
        return response


class WebDownloadFile(viewsets.ViewSet):
    @method_decorator(loginAuth)
    def list(self, request):
        '''
        获取某个文件或目录的属性信息。
        '''
        inputData = request.GET
        keyList = ['platform', 'username', 'encrypedToken', 'timestamp', 'serverPath']
        checkKeys = CheckKeys(inputData, keyList)
        if not checkKeys['status'] == 0:
            lackKey = checkKeys['lackKey']
            return GenerateFailedResponse(generateError('paramLack', lackKey))
        user = inputData.get("username")
        cluster = inputData.get("cluster")
        ################   ↑↑↑↑↑↑   以上常规检查工作结束   ↑↑↑↑↑↑   ###################
        serverPath = request.GET.get('serverPath').replace('\\', '/')
        fileName = os.path.basename(serverPath)
        fileSize = ''
        # 获取可选参数

        # 通过SDK，访问资源层接口
        def file_iterator():
            client = THSClient(config['appid'], config['appkey'], config['server'], cluster, user, serverPath)
            fileSize = 0
            try:
                objs = client.getObjectMeta()
                fileSize = objs['size']
            except Exception as e:
                print
                e
                # return Response({"success":"no",
                #                "error_desc":eval(str(e))['Message']})
            limit = 1048576
            chunkNum = 0
            while True:
                offset = chunkNum * limit
                if (fileSize - offset < limit):
                    limit = fileSize - offset
                try:
                    c = client.getObject(limit=limit, offset=offset)
                    yield c
                except Exception as e:
                    print
                    e
                    # return Response({"success":"no",
                    #                "error_desc":eval(str(e))['Message']})
                if (fileSize - offset == limit):
                    break
                chunkNum += 1

        response = FileResponse(file_iterator())
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = 'attachment;filename="{0}"'.format(fileName).encode('utf-8')
        response['Content-Length'] = fileSize  # 传输给客户端的文件大小
        response['filename'] = fileName.encode('utf-8')
        return response

        # 本次已将下载接口修改为GET，因此无需再使用如下方法。
        # 如果下载接口以POST的方法提供，则前台的下载可能会遇到问题。此时，可以用如下方法，先将下载文件放到static下一个临时目录中，然后将该路径生成一个下载链接，返回给客户端进行下载。
        # 生成链接文件路径和临时下载链接
        # todayDate = datetime.date.today().strftime('%Y%m%d')
        # encrypedTodayDate = hashlib.md5(todayDate).hexdigest()          # 为方便后期清除，所有连接文件均放在以当前日期命名的目录下，为不暴露，当天日期需经md5加密处理
        # BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        # STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
        # todayDatePath = os.path.join(STATIC_ROOT, encrypedTodayDate)        #当天日期路径
        # randomStr = hashlib.md5(str(uuid.uuid1())).hexdigest()
        # linkFileFolder = os.path.join(todayDatePath, randomStr)              #链接文件所在目录
        # linkFilePath = os.path.join(linkFileFolder, fileName)                #链接文件全路径
        # tmpLink = os.path.join('https://wp.th-icloud.cn/static', encrypedTodayDate, randomStr, fileName)                         #临时下载链接

        # mkdirCommand = "mkdir -p %s" % linkFileFolder
        # try:
        #     if not os.path.exists(linkFileFolder):
        #         result = os.system(mkdirCommand)
        #         if not result == 0:
        #             return GenerateFailedResponse(generateError('mkdirFailed'))
        # except Exception:
        #     return GenerateFailedResponse(generateError('mkdirFailed'))
        # lnCommand = "ln -s %s %s" % (sourcePath, linkFilePath)
        # try:
        #     result = os.system(lnCommand)
        #     if not result == 0:
        #         return GenerateFailedResponse(generateError('generateTmpLinkFailed'))
        # except Exception:
        #     return GenerateFailedResponse(generateError('generateTmpLinkFailed'))

        # return Response({"success":"yes", "tmpLink":tmpLink})

@login_required
def thstorage(request):
    return render(request, "home.html")