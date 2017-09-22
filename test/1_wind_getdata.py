# -*- coding: utf-8 -*-
# @Author: jrcaiwenxi
# @Date:   2017-05-11 18:50:56
# @Last Modified by:   jrcaiwenxi
# @Last Modified time: 2017-05-12 18:36:43
from WindPy import w

w.start()

# 命令如何写可以用命令生成器来辅助完成
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


# 通过wset来取数据集数据
print('\n\n' + '-----通过wset来取数据集数据,获取中小板指数权重-----' + '\n')
wsetdata = w.wset("IndexConstituent",
                  "date=20170511;windcode=399006.SZ;field=date,wind_code,i_weight")
printpy(wsetdata)
