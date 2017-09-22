# -*- coding: utf-8 -*-
# @Author: jrcaiwenxi
# @Date:   2017-05-12 16:25:12
# @Last Modified by:   jrcaiwenxi
# @Last Modified time: 2017-05-18 17:55:30
# 初始化接口

from WindPy import *
import json
import datetime


# 自定义DateTime的输出函数，避免Python自带的json序列化工具不能序列化datetime类型数据问题
class CJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, date):
            return obj.strftime('%Y-%m-%d')
        else:
            return json.JSONEncoder.default(self, obj)


# 定义打印输出函数，用来展示数据使用
def printpy(outdata):
    if outdata.ErrorCode != 0:
        print('error code:' + str(outdata.ErrorCode) + '\n')
        return()
    for i in range(0, len(outdata.Data[0])):
        strTemp = ''
        if len(outdata.Times) > 1:
            strTemp = str(outdata.Times[i]) + ' '
        for k in range(0, len(outdata.Fields)):
            strTemp = strTemp + str(outdata.Data[k][i]) + ' '
        print(strTemp)


w.start()

# 获取中小盘指数代码#
All399005Stock = w.wset(
    "IndexConstituent", "date=20170518;windcode=399005.SZ;field=date,wind_code,i_weight")
if All399005Stock.ErrorCode != 0:
    print("Get Data failed! exit!")
    exit()
# printpy(All399005Stock)

# 保存股票代码到文件中#
jfile = '20170518_399005_date_code_weight.json'
with open(jfile, mode='w') as f:
    # saveJson(All399005Stock, f)
    json.dump(All399005Stock.Data, f, cls=CJsonEncoder)

# 打开读一下
with open(jfile, 'r') as f:
    MyData = json.load(f)
print(MyData)
