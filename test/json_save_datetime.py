# -*- coding: utf-8 -*-
# @Author: jrcaiwenxi
# @Date:   2017-05-24 17:33:00
# @Last Modified by:   jrcaiwenxi
# @Last Modified time: 2017-05-24 17:51:48
import json
import datetime


# 自定义DateTime的输出函数，避免Python自带的json序列化工具不能序列化datetime类型数据问题
class CJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, datetime.date):
            return obj.strftime('%Y-%m-%d')
        else:
            return json.JSONEncoder.default(self, obj)
