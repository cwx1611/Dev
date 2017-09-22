# -*- coding: utf-8 -*-
# @Author: jrcaiwenxi
# @Date:   2017-05-19 10:43:26
# @Last Modified by:   jrcaiwenxi
# @Last Modified time: 2017-05-19 18:33:06
from WindPy import *
import datetime
import time
w.start()

# open a file to write.
pf = open('20170519_pywsqdataif.data', 'w')
midday = datetime.datetime(2017, 5, 19, 14, 00, 0, 0)
go_on = True
# define the callback function
# 用于处理行情的回调函数


def myCallback(indata):
    print(indata)

    if indata.ErrorCode != 0:
        print('error code:' + str(indata.ErrorCode) + '\n')
        return()

    global begintime
    lastvalue = ""
    for k in range(0, len(indata.Fields)):
        if(indata.Fields[k] == "RT_TIME"):
            begintime = indata.Data[k][0]
        if(indata.Fields[k] == "RT_LAST"):
            lastvalue = str(indata.Data[k][0])

    string = str(begintime) + " " + lastvalue + "\n"
    pf.writelines(string)
    print(string)
    pf.flush()

    # 想要结束订阅，可使用w.cancelRequest(0)命令，然后后调用pf.close()关闭文件
    # pf.close()
    now = datetime.datetime.now()
    print('now = ' + str(now))
    if now > midday:
        w.cancelRequest(0)
        pf.close()
        global go_on
        go_on = False
        print('cancel all the request')
    else:
        print('gogogo')


# 订阅行情
w.wsq("002555.SZ", "rt_time,rt_last", func=myCallback)
while(go_on):
    print('First go on is')
    print(go_on)
    info = "这个while循环主要是防止IDE在运行或者debug时，运行w.wsq()语句后就退出，从而导致行情推送过来后，回调函数无法运行！"
    print(info)
    time.sleep(2)
    print('Then go on is')
    print(go_on)
    if(not go_on):
        break
    else:
        pass
