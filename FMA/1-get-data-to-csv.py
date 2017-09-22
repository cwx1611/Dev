# -*- coding: utf-8 -*-
# @Author: jrcaiwenxi
# @Date:   2017-09-10 11:20:18
# @Last Modified by:   jrcaiwenxi
# @Last Modified time: 2017-09-10 11:27:26
from WindPy import w
import pandas as pd
import json
w.start()

# 取数据的命令如何写可以用命令生成器来辅助完成
# 开盘价、收盘价、最低价、最高价、成交股数、成交金额、成交笔数、涨跌（金额）、涨跌百分比、平均成交价、换手率
wsd_data = w.wsd("002555.SZ", "open,high,low,close,volume,amt,dealnum,chg,pct_chg,vwap,turn",
                 "2017-08-12", "2017-08-18", "PriceAdj=F")

# 演示如何将api返回的数据装入Pandas的Series
open = pd.Series(wsd_data.Data[0])
high = pd.Series(wsd_data.Data[1])
low = pd.Series(wsd_data.Data[2])
close = pd.Series(wsd_data.Data[3])

print('open:/n', open)
print('high:/n', high)
print('low:/n', low)
print('close:/n', close)

# 演示如何将api返回的数据装入Pandas的DataFrame
fm = pd.DataFrame(wsd_data.Data, index=wsd_data.Fields, columns=wsd_data.Times)
fm = fm.T  # 将矩阵转置
print('fm:/n', fm)