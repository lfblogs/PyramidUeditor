#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Language Version: 3.4.x
# Last Modified: 2015-06-04 11:45:15


__all__ = []
__author__ = "lfblogs (email:13701242710@163.com)"
__version__ = "1.0.1"
from .views import ueditor,ueditorupload
def includeme(config):
    config.add_route('ueditor', '/ueditor/')
    config.add_route('ueditorupload', '/ueditorupload/')

    config.add_view(ueditor,
                 route_name='ueditor',
                 renderer='templates/ueditor.pt')
    config.add_view(ueditorupload,
                 route_name='ueditorupload')