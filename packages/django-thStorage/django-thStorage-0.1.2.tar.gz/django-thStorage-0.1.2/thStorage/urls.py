#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/12/16 11:14
# @Author : tianyang@nscc-tj.gov.cn
# @About.:.
# @File : urls.py
# @Site : 
# @Software: PyCharm

from django.conf.urls import include, url
from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import *

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'updateQuota', UpdateQuota, 'UpdateQuota')
router.register(r'list', ContentList, 'ContentList')
router.register(r'capacity', Capacity, 'Capacity')
router.register(r'newfolder', NewFolder, 'NewFolder')
router.register(r'newFile', NewFile, 'NewFile')
router.register(r'delete', Delete, 'Delete')
router.register(r'copyTo', CopyTo, 'CopyTo')
router.register(r'cutTo', CutTo, 'CutTo')
router.register(r'rename', Rename, 'Rename')
router.register(r'attribute', Attribute, 'Attribute')
router.register(r'webUploadFile', webUploadFile, 'webUploadFile')
#router.register(r'uploadFile', UploadFile, base_name='UploadFile')
router.register(r'downloadFile', DownloadFile, 'DownloadFile')
router.register(r'webDownloadFile', WebDownloadFile, 'WebDownloadFile')

urlpatterns = [
    url(r'^', include(router.urls)),
    path('thstorage/', thstorage),
]