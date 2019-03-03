import pandas as pd
import tushare as ts
from statsmodels.tsa.stattools import adfuller
from numpy import std, subtract, polyfit, sqrt, log

"""
ADF test沪深300
"""
path = ('H:/software/work/python_project/PythonStudyDemo/quant/csv/hs300_D/{}.csv')

def ADF(symbol):
    df = pd.read_csv(path.format(symbol))
    res = adfuller(df['pre_close'])
    # 小于1% 且 p.value 接近0
    if res[0] < res[4]['1%'] and ((res[1] > 0 and res[1] < 1) or (res[1] < 0 and res[1] > -1)):
        return True
    else:
        return False


def hurst(symbol):
    df = pd.read_csv(path.format(symbol))
    ts=df['pre_close']
    # create the range of lag values
    i = len(ts) // 2
    lags = range(2, i)
    # Calculate the array of the variances of the lagged differences
    tau = [sqrt(std(subtract(ts[lag:], ts[:-lag]))) for lag in lags]

    # use a linear fit to estimate the Hurst Exponent
    poly = polyfit(log(lags), log(tau), 1)
    return poly[0] * 2.0
    # Return the Hurst Exponent from the polyfit output


if __name__ == "__main__":
    pro = ts.pro_api()
    data = pro.stock_basic(exchange_id='', list_status='L',
                           fields='symbol,name')
    symbols = data['symbol'][:]
    success = []
    try:
        # names=data['name'][:24]
        for symbol in symbols:
            print(symbol)
            res=hurst(symbol)
            success.append("Hurst(%s):" % res)
    except Exception as e:
        print(e)
        pass
    print(success)
