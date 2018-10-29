"""
通过tushare获取沪深300
"""
import numpy as np
import tushare as ts



pro = ts.pro_api()

#查询当前所有正常上市交易的股票列表

data = pro.stock_basic(exchange_id='', list_status='L',
                       fields='ts_code,symbol,name,area,industry,list_date')
symbols=data['symbol']
#遍历获取数据
for symbol in symbols:
    print(symbol)
    ts_code=symbol
    if symbol.startswith("3") or symbol.startswith("0"):
        ts_code='%s.SZ'%ts_code
        continue
    else:
        ts_code='%s.SH'%ts_code
    hist_data=pro.daily(ts_code=ts_code)
    hist_data['price_date']=hist_data['trade_date']
    hist_data['data_vendor_id']=np.full(len(hist_data.index),2,int)
    hist_data['symbol_id']=hist_data['ts_code']
    print(hist_data.head())
    #选择保存
    hist_data.to_csv(
        'H:\software\work\python_project\PythonStudyDemo\quant\csv\hs300_D\%s.csv'%symbol
        ,columns=['data_vendor_id','symbol_id','price_date','open','high','low','close','pre_close','vol'])
