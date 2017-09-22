# -*- coding: utf-8 -*-
# @Author: jrcaiwenxi
# @Date:   2017-05-11 18:09:22
# @Last Modified by:   jrcaiwenxi
# @Last Modified time: 2017-05-26 14:05:02
import datetime

midday = datetime.datetime(2017, 5, 19, 11, 30, 0, 0)

print("hello")
now = datetime.datetime.now()
print(now)
if(now <= midday):
    print('wait')
else:
    print('pass')


def scopetest():
    var = 6
    print(var)


var = 5
print(var)
scopetest()
print(var)
