#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Language Version: 3.4.x
# Last Modified: 2015-06-04 11:45:15


__all__ = []
__author__ = "lfblogs (email:13701242710@163.com)"
__version__ = "1.0.1"


import json
import re

from pyramid.view import view_config
from pyramid.response import Response

from .utils import Uploader
from .settings import JSON_CONFIG,JSON_FILE,UEDITOR_UPLOAD_ROOT


def ueditor(request):
    return {}   

def ueditorupload(request):
    """
        UEditor文件上传接口
        SETTINGS 实例化传入的配置项
        result 返回结果
    """

    minetype = 'application/json'
    result = {}
    action = request.GET.get('action')

    
    #获取UeSettings的配置信息,如为空，将尝试读取JSON配置文件
    SETTINGS = JSON_CONFIG
    if SETTINGS is {}:
        
        with open(JSON_FILE) as fp:
            try:
                #删除 '/**/'之间的注释
                SETTINGS = json.loads(re.sub(r'\/\*.*\/','',fp.read()))
            except:
                SETTINGS = {}

    if action == 'config':
        #初始化返回配置项给客户端
        result = SETTINGS
    elif action in ('uploadimage','uploadfile','uploadvideo'):
        #上传图片、视频、文件
        if action == 'uploadimage':
            FieldName = SETTINGS.get('imageFieldName')
            settings = {
                "pathFormat" : SETTINGS.get('imagePathFormat'),
                "maxSize" : SETTINGS.get('imageMaxSize'),
                "allowFiles" : SETTINGS.get('imageAllowFiles'),
                }
        
        elif action == 'uploadvideo':
            FieldName = SETTINGS.get('videoFieldName')
            settings = {
                "pathFormat" : SETTINGS.get('videoPathFormat'),
                "maxSize" : SETTINGS.get('videoMaxSize'),
                "allowFiles" : SETTINGS.get('videoAllowFiles'),
                }

        else:
            FieldName = SETTINGS.get('fileFieldName')
            settings = {
                "pathFormat" : SETTINGS.get('filePathFormat'),
                "maxSize" : SETTINGS.get('fileMaxSize'),
                "allowFiles" : SETTINGS.get('fileAllowFiles'),
                }

        if FieldName in request.params:
            Field = request.params[FieldName]
            uploader = Uploader(Field,settings,UEDITOR_UPLOAD_ROOT)
            result = uploader.getFileInfo()
        else:
            result['state'] = '上传接口错误'

    elif action in ('uploadscrawl'):
        #上传涂鸦
        FieldName = SETTINGS.get('scrawlFieldName')
        settings = {
            "pathFormat": SETTINGS.get('scrawlPathFormat'),
            "maxSize": SETTINGS.get('scrawlMaxSize'),
            "allowFiles": SETTINGS.get('scrawlAllowFiles'),
            "oriName": "scrawl.png"
            }
 
        if FieldName in request.params:
            Field = request.params[FieldName]
            uploader = Uploader(Field,settings,UEDITOR_UPLOAD_ROOT,'base64')
            result = uploader.getFileInfo()
        else:
            result['state'] = '上传接口错误'          

    elif action in ('catchimage'):
        #截图上传
        FieldName = SETTINGS.get('catcherFieldName')
        settings = {
            "pathFormat": SETTINGS.get('catchPathFormat'),
            "maxSize": SETTINGS.get('catchMaxSize'),
            "allowFiles": SETTINGS.get('catchAllowFiles'),
            "oriName": "remote.png"
            }

        if FieldName in request.params:
            source = []
        elif '%s[]' % FieldName in request.params:
            source = request.params.getlist('%s[]' % FieldName)

        _list = []
        for imgurl in source:
            uploader = Uploader(imgurl,settings,UEDITOR_UPLOAD_ROOT,'remote')
            info = uploader.getFileInfo()
            _list.append({
                'state' : info['state'],
                'url' : info['url'],
                'original' : info['original'],
                'source' : imgurl,
                })

        result['state'] = 'SUCCESS' if len(_list) >0 else 'ERROR'
        result['list'] = _list

    else:
        result['state'] = '服务器请求接口错误'

    result = json.dumps(result)

    if 'callback' in request.GET:
        callback = request.GET.get('callback')
        if re.match(r'^[\w_]+$',callback):
            result = '%s(%s)' % (callback,result)
            minetype = 'application/javascript'
        else:
            result = json.dumps({'state' : 'callback参数不符合规则'})

    resp = Response(result)
    resp.minetype = minetype
    resp.headers['Access-Control-Allow-Origin'] = '*'
    resp.headers['Access-Control-Allow-Headers'] = 'X-Requested-With,X_Requested_With'
    return resp
        
            
        
