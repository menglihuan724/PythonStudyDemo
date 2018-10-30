import datetime
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
import pandas_datareader.data as web
import pprint
import statsmodels.tsa.stattools as ts
import statsmodels.api as sm
import tushare as tss

path = ('H:/software/work/python_project/PythonStudyDemo/quant/csv/hs300_D/{}.csv')


def plot_price_series(df, ts1, ts2):
    months = mdates.MonthLocator()  # every month
    fig, ax = plt.subplots()
    ax.plot(df.index, df[ts1], label=ts1)
    ax.plot(df.index, df[ts2], label=ts2)
    ax.xaxis.set_major_locator(months)
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))
    ax.set_xlim(datetime.datetime(2018, 1, 1), datetime.datetime(2018, 10, 24))
    ax.grid(True)
    fig.autofmt_xdate()

    plt.xlabel('Month/Year')
    plt.ylabel('Price ($)')
    plt.title('%s and %s Daily Prices' % (ts1, ts2))
    plt.legend()
    plt.show()


def plot_scatter_series(df, ts1, ts2):
    plt.xlabel('%s Price ($)' % ts1)
    plt.ylabel('%s Price ($)' % ts2)
    plt.title('%s and %s Price Scatterplot' % (ts1, ts2))
    plt.scatter(df[ts1], df[ts2])
    plt.show()


def plot_residuals(df):
    months = mdates.MonthLocator()  # every month
    fig, ax = plt.subplots()
    ax.plot(df.index, df["res"], label="Residuals")
    ax.xaxis.set_major_locator(months)
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))
    ax.set_xlim(datetime.datetime(2018, 1, 1), datetime.datetime(2018, 10, 24))
    ax.grid(True)
    fig.autofmt_xdate()

    plt.xlabel('Month/Year')
    plt.ylabel('Price ($)')
    plt.title('Residual Plot')
    plt.legend()

    plt.plot(df["res"])
    plt.show()


if __name__ == "__main__":
    # start = datetime.datetime(2018, 1, 1)
    # end = datetime.datetime(2018, 10, 24)
    #
    # arex = web.DataReader("AREX", "yahoo", start, end)
    # SLB = web.DataReader("SLB", "yahoo", start, end)

    pro = tss.pro_api()
    data = pro.stock_basic(exchange_id='', list_status='L',
                           fields='symbol,name')
    symbols = data['symbol']
    names=data['name']
    success = []
    try:
        for indexa,symbola in enumerate(symbols):
            a=pd.read_csv(path.format(symbola))
            df = pd.DataFrame(index=a.index)
            first_name=names[indexa]
            df[first_name] = a["pre_close"]

            for indexb,symbolb in enumerate(symbols):

                if symbola!=symbolb:

                    second_name=names[indexa]

                    b=pd.read_csv(path.format(symbolb))
                    df[second_name] = b["pre_close"]

                    # Plot the two time series
                    # plot_price_series(df, first_name, second_name)

                    # Display a scatter plot of the two time series
                    # plot_scatter_series(df, first_name, second_name)

                    # Calculate optimal hedge ratio "beta"
                    x = sm.add_constant(df[first_name])
                    model = sm.OLS(endog=df[second_name], exog=x)
                    res = model.fit()
                    # beta_hr = res.params

                    # Calculate the residuals of the linear combination
                    df["res"] = df[second_name] - res.params[1] * df[first_name]

                    # Plot the residuals
                    # plot_residuals(df)

                    # Calculate and output the CADF test on the residuals
                    cadf = ts.adfuller(df["res"])
                    # pprint.pprint(cadf)
                    if cadf[0]<0.5:
                        success.append(f'组合:{first_name}:{second_name}')
    except Exception as e:
            print(e)
            pass



    print(success)