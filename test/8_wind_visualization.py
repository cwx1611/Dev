# -*- coding: utf-8 -*-
# @Author: jrcaiwenxi
# @Date:   2017-05-19 18:53:34
# @Last Modified by:   jrcaiwenxi
# @Last Modified time: 2017-05-23 18:21:32
from WindPy import *
import pandas as pd
import matplotlib.pylab as plt
from matplotlib.finance import candlestick_ohlc
from matplotlib.dates import date2num
from matplotlib.font_manager import FontProperties

font = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=14)
w.start()

dat = w.wsd("002555.SZ", "open,high,low,close,volume,amt", "2017-05-10",
            "2017-05-23", "TradingCalendar=SZSE;Fill=Previous")

fm = pd.DataFrame(dat.Data, index=dat.Fields,
                  columns=dat.Times)  # pandas timeseries type
fm = fm.T

type(fm['OPEN'])


fm['CLOSE'].plot(color='purple')
plt.show()

fig, ax = plt.subplots()
ax.plot(fm['OPEN'])
ax.set_xticklabels(fm.index.date, rotation=30)
plt.ylabel('price')
plt.title(u'三七互娱', fontproperties=font)
plt.show()


# 带成交量k线图 http://www.360doc.com/content/16/0411/23/7249274_549857456.shtml
fig = plt.figure()
ax1 = plt.subplot2grid((4, 4), (0, 0), rowspan=3, colspan=4)
ohlc = zip(fm.index.map(date2num), fm['OPEN'], fm[
           'HIGH'], fm['LOW'], fm['CLOSE'])
candlestick_ohlc(ax1, ohlc, width=0.4, colorup='#77d879', colordown='#db3f3f')
plt.grid(True)

ax2 = plt.subplot2grid((4, 4), (3, 0), rowspan=1, colspan=4)
ax2.bar(fm.index.map(date2num), fm['VOLUME'], width=0.4, align='center')
plt.grid(True)

ax2.set_xticklabels(fm.index.date, rotation=30)
plt.setp(ax1.get_xticklabels(), visible=True)
plt.setp(ax1.yaxis.get_ticklabels()[0], visible=True)
plt.show()


# 双y轴 http://www.financecomputing.net/wordpress/?p=1093
ax2 = ax1.twinx()
