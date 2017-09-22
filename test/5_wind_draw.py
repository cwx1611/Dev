# -*- coding: utf-8 -*-
# @Author: jrcaiwenxi
# @Date:   2017-05-19 18:34:22
# @Last Modified by:   jrcaiwenxi
# @Last Modified time: 2017-05-19 18:39:11
from WindPy import *
import pandas as pd
import matplotlib.pylab as plt

w.start()

dat = w.wsd("002555.SZ", "open,high,low,close,volume,amt", "2017-05-13",
            "2017-05-19", "TradingCalendar=SZSE;Fill=Previous")

fm = pd.DataFrame(dat.Data, index=dat.Fields, columns=dat.Times)  # pandas timeseries type
fm = fm.T

type(fm['OPEN'])

fm['CLOSE'].plot(color='green')
plt.show()
