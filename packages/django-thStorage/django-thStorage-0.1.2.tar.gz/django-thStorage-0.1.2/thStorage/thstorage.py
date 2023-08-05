import hashlib
import time
import uuid
import requests

from rest_framework.response import Response
from django.conf import settings
from .errorList import *
from .models import *

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

def loginAuth(func):
    '''验证登录装饰器，
    :param func:
    :return:
    '''
    def wrapper(request,*args,**kwargs):
        if request.method == "GET":
            inputData = request.GET
        else:
            inputData = request.data
        platform = inputData.get("platform", settings.TH_STORAGE_CONFIG.get("PLATFORM", "default"))
        cluster = inputData.get("cluster","")
        username = inputData.get('username', '')
        encrypedToken = inputData.get('encrypedToken', '')
        timestamp = inputData.get('timestamp', 0)
        cluster = inputData.get('cluster','')
        # 判断当前时间戳，与timestamp做差值，如差值在1分钟以上，则报错timestampNotFit
        nowTimestamp = int(time.time())
        config = settings.TH_STORAGE_CONFIG
        print(cluster + username)
        if abs(nowTimestamp - int(timestamp)) > config['TOKEN_UPDATE_IMTERVAL']:
            return GenerateFailedResponse(generateError('timestampNotFit'))
        if not NetDiskUser.objects.filter(cluster=cluster, systemUsername=username):
            return GenerateFailedResponse(generateError('UsernameNotExist', username))
        if len(NetDiskUser.objects.filter(cluster=cluster, systemUsername=username)) > 1:
            return GenerateFailedResponse(generateError('UsernameRepeat', username))
        userInfo = NetDiskUser.objects.filter(cluster=cluster, systemUsername=username).first()
        token = userInfo.token
        tokenGererateTime = userInfo.tokenGererateTime
        tokenValidityPeriod = userInfo.tokenValidityPeriod
        if nowTimestamp > (tokenGererateTime + tokenValidityPeriod):
            return GenerateFailedResponse(generateError('tokenTimeOut', username))
        combToken = str(token) + str(timestamp)
        if not encrypedToken == hashlib.sha256(combToken.encode("utf8")).hexdigest():
            return GenerateFailedResponse(generateError('wrongToken', username))
        return func(request, *args, **kwargs)
    return wrapper

class THStorageUser:
    def __init__(self,username,cluster,systemUsername):
        self.username = username
        self.cluster = cluster
        self.systemUsername = systemUsername

    def GenerateToken(self):
        '''
        生成一个32位的随机令牌
        '''
        random_str = str(uuid.uuid1())
        m = hashlib.md5()
        m.update(random_str.encode("utf8"))
        token = m.hexdigest()
        tokenGererateTime = int(time.time())
        tokenValidityPeriod = time.time() + settings.TH_STORAGE_CONFIG.get("TOKEN_UPDATE_IMTERVAL",36000000)
        return token,tokenGererateTime,tokenValidityPeriod

    def Login(self):
        user = NetDiskUser.objects.filter(username=self.username,systemUsername=self.systemUsername).first()
        token,tokenGererateTime,tokenValidityPeriod = self.GenerateToken()
        if not user:
            newUser = NetDiskUser(username=self.username,systemUsername=self.systemUsername,cluster=self.cluster)
            newUser.save()
        else:
            NetDiskUser.objects.filter(username=self.username, systemUsername=self.systemUsername).update(token=token,tokenGererateTime=tokenGererateTime,tokenValidityPeriod=tokenValidityPeriod)

        return token,self.username,self.cluster,self.systemUsername

class THSClient:
    def __init__(self, appid, appkey, server, cluster, user, path, timeout=60, chunk_size=65536):
        self.appid = appid
        self.appkey = appkey
        self.server = server
        self.cluster = cluster
        self.user = user
        self.path = path
        self.timeout = timeout
        self.chunk_size = chunk_size

    def _make_sig(self, timestamp):
        str1 = "appkey=%s&timestamp=%s&cluster=%s&user=%s&path=%s" % (
            self.appkey, timestamp, self.cluster, self.user, self.path)
        hashStr = hashlib.sha256()
        hashStr.update(str1.encode())
        sig = hashStr.hexdigest()
        return sig

    def listObjects(self, sort="modify", desc=1, page=1, count=0, search=""):
        url = "%s/v1/%s/%s/storage/listObject?appid=%s&sort=%s&desc=%s&page=%s&count=%s&search=%s" % (
            self.server, self.cluster, self.user, self.appid, sort, desc, page, count, search)
        timestamp = int(time.time())
        data = {
            "path": self.path,
            "sig": self._make_sig(timestamp),
            "timestamp": timestamp,
        }

        resp = requests.post(url=url, data=data, timeout=self.timeout)

        if resp.status_code < 300:
            return resp.json()
        else:
            raise ValueError(resp.json())

    def createObject(self, dir=0):
        url = "%s/v1/%s/%s/storage/createObject?appid=%s&dir=%s" % (
        self.server, self.cluster, self.user, self.appid, dir)
        timestamp = int(time.time())
        data = {
            "path": self.path,
            "sig": self._make_sig(timestamp),
            "timestamp": timestamp,
        }

        resp = requests.post(url=url, data=data, timeout=self.timeout)

        if resp.status_code < 300:
            return {}
        else:
            raise ValueError(resp.json())

    def getObjectMeta(self):
        url = "%s/v1/%s/%s/storage/getObjectMeta?appid=%s" % (
            self.server, self.cluster, self.user, self.appid)
        timestamp = int(time.time())
        data = {
            "path": self.path,
            "sig": self._make_sig(timestamp),
            "timestamp": timestamp,
        }

        resp = requests.post(url=url, data=data, timeout=self.timeout)

        if resp.status_code < 300:
            return resp.json()
        else:
            raise ValueError(resp.json())

    def copyObject(self, sourcePath, recursive=0):
        url = "%s/v1/%s/%s/storage/copyObject?appid=%s&recursive=%s" % (
            self.server, self.cluster, self.user, self.appid, recursive)
        timestamp = int(time.time())
        data = {
            "path": self.path,
            "sig": self._make_sig(timestamp),
            "timestamp": timestamp,
            "sourcePath": sourcePath
        }

        resp = requests.post(url=url, data=data, timeout=self.timeout)

        if resp.status_code < 300:
            return {}
        else:
            raise ValueError(resp.json())

    def moveObject(self, sourcePath, recursive=0):
        url = "%s/v1/%s/%s/storage/moveObject?appid=%s&recursive=%s" % (
            self.server, self.cluster, self.user, self.appid, recursive)
        timestamp = int(time.time())
        data = {
            "path": self.path,
            "sig": self._make_sig(timestamp),
            "timestamp": timestamp,
            "sourcePath": sourcePath
        }

        resp = requests.post(url=url, data=data, timeout=self.timeout)

        if resp.status_code < 300:
            return {}
        else:
            raise ValueError(resp.json())

    def deleteObject(self, recursive=0):
        url = "%s/v1/%s/%s/storage/deleteObject?appid=%s&recursive=%s" % (
            self.server, self.cluster, self.user, self.appid, recursive)
        timestamp = int(time.time())
        data = {
            "path": self.path,
            "sig": self._make_sig(timestamp),
            "timestamp": timestamp,
        }

        resp = requests.post(url=url, data=data, timeout=self.timeout)

        if resp.status_code < 300:
            return {}
        else:
            raise ValueError(resp.json())

    def getObject(self, limit=0, offset=0):
        url = "%s/v1/%s/%s/storage/getObject?appid=%s&limit=%s&offset=%s" % (
            self.server, self.cluster, self.user, self.appid, limit, offset)
        timestamp = int(time.time())
        data = {
            "path": self.path,
            "sig": self._make_sig(timestamp),
            "timestamp": timestamp,
        }

        resp = requests.post(url=url, data=data, timeout=self.timeout)

        if resp.status_code < 300:
            return resp.content
        else:
            raise ValueError(resp.json())

    def putObject(self, file):
        url = "%s/v1/%s/%s/storage/putObject?appid=%s" % (self.server, self.cluster, self.user, self.appid)
        timestamp = int(time.time())
        data = {
            "path": self.path,
            "sig": self._make_sig(timestamp),
            "timestamp": timestamp,
        }
        files = {'file': file}

        resp = requests.post(url=url, data=data, files=files, timeout=self.timeout)

        if resp.status_code < 300:
            return {}
        else:
            raise ValueError(resp.json())

    def appendObject(self, file):
        url = "%s/v1/%s/%s/storage/appendObject?appid=%s" % (self.server, self.cluster, self.user, self.appid)
        timestamp = int(time.time())
        data = {
            "path": self.path,
            "sig": self._make_sig(timestamp),
            "timestamp": timestamp,
        }
        files = {'file': file}

        resp = requests.post(url=url, data=data, files=files, timeout=self.timeout)

        if resp.status_code < 300:
            return {}
        else:
            raise ValueError(resp.json())