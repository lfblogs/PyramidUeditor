#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Language Version: 3.4.x
# Last Modified: 2015-06-04 11:45:15


__all__ = []
__author__ = "lfblogs (email:13701242710@163.com)"
__version__ = "1.0.1"

import os

UEDITOR_UPLOAD_ROOT = os.path.dirname(__file__) #upload files  root
UEDITOR_STATIC_ROOT = os.path.join(os.path.dirname(__file__),'static') #ueditor static files root
JSON_FILE = os.path.join(os.path.dirname(__file__),'static/ueditor/php/config.json')

JSON_CONFIG = {

    "imageActionName": "uploadimage",
    "imageFieldName": "upfile", 
    "imageMaxSize": 2048000, 
    "imageAllowFiles": [".png", ".jpg", ".jpeg", ".gif", ".bmp"], 
    "imageCompressEnable": 1, 
    "imageCompressBorder": 1600, 
    "imageInsertAlign": "none", 
    "imageUrlPrefix": "", 
    "imagePathFormat": "/static/upload/image/{yyyy}{mm}{dd}/{time}{rand:6}", 

    "scrawlActionName": "uploadscrawl",
    "scrawlFieldName": "upfile", 
    "scrawlPathFormat": "/static/upload/image/{yyyy}{mm}{dd}/{time}{rand:6}",
    "scrawlMaxSize": 2048000,
    "scrawlUrlPrefix": "", 
    "scrawlInsertAlign": "none",

    "snapscreenActionName": "uploadimage", 
    "snapscreenPathFormat": "/static/upload/image/{yyyy}{mm}{dd}/{time}{rand:6}", 
    "snapscreenUrlPrefix": "", 
    "snapscreenInsertAlign": "none", 


    "catcherLocalDomain": ["127.0.0.1", "localhost", "img.baidu.com"],
    "catcherActionName": "catchimage",
    "catcherFieldName": "source",
    "catcherPathFormat": "/static/upload/image/{yyyy}{mm}{dd}/{time}{rand:6}",
    "catcherUrlPrefix": "",
    "catcherMaxSize": 2048000,
    "catcherAllowFiles": [".png", ".jpg", ".jpeg", ".gif", ".bmp"],


    "videoActionName": "uploadvideo", 
    "videoFieldName": "upfile", 
    "videoPathFormat": "/static/upload/video/{yyyy}{mm}{dd}/{time}{rand:6}",
    "videoUrlPrefix": "", 
    "videoMaxSize": 102400000, 
    "videoAllowFiles": [
        ".flv", ".swf", ".mkv", ".avi", ".rm", ".rmvb", ".mpeg", ".mpg",
        ".ogg", ".ogv", ".mov", ".wmv", ".mp4", ".webm", ".mp3", ".wav", ".mid"], 


    "fileActionName": "uploadfile", 
    "fileFieldName": "upfile",
    "filePathFormat": "/static/upload/file/{yyyy}{mm}{dd}/{time}{rand:6}", 
    "fileUrlPrefix": "",
    "fileMaxSize": 51200000,
    "fileAllowFiles": [
        ".png", ".jpg", ".jpeg", ".gif", ".bmp",
        ".flv", ".swf", ".mkv", ".avi", ".rm", ".rmvb", ".mpeg", ".mpg",
        ".ogg", ".ogv", ".mov", ".wmv", ".mp4", ".webm", ".mp3", ".wav", ".mid",
        ".rar", ".zip", ".tar", ".gz", ".7z", ".bz2", ".cab", ".iso",
        ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx", ".pdf", ".txt", ".md", ".xml"
    ], 

    
    "imageManagerActionName": "listimage", 
    "imageManagerListPath": "/static/upload/image/", 
    "imageManagerListSize": 20, 
    "imageManagerUrlPrefix": "", 
    "imageManagerInsertAlign": "none",
    "imageManagerAllowFiles": [".png", ".jpg", ".jpeg", ".gif", ".bmp"],

  
    "fileManagerActionName": "listfile", 
    "fileManagerListPath": "/static/upload/file/", 
    "fileManagerUrlPrefix": "",
    "fileManagerListSize": 20, 
    "fileManagerAllowFiles": [
        ".png", ".jpg", ".jpeg", ".gif", ".bmp",
        ".flv", ".swf", ".mkv", ".avi", ".rm", ".rmvb", ".mpeg", ".mpg",
        ".ogg", ".ogv", ".mov", ".wmv", ".mp4", ".webm", ".mp3", ".wav", ".mid",
        ".rar", ".zip", ".tar", ".gz", ".7z", ".bz2", ".cab", ".iso",
        ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx", ".pdf", ".txt", ".md", ".xml"
    ] 

}
