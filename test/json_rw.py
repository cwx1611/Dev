# -*- coding: utf-8 -*-
# @Author: jrcaiwenxi
# @Date:   2017-05-24 19:02:44
# @Last Modified by:   jrcaiwenxi
# @Last Modified time: 2017-08-24 10:52:50
import json

# 保存股票代码到文件中#
jfile = '20170714_002555_wsi_data.json'

# 打开读一下
with open(jfile, 'r') as f:
    MyData = json.load(f)
print(MyData)
