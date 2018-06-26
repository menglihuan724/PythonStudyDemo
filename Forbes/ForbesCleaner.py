import pandas as pd
import numpy as np

np.set_printoptions(threshold=np.inf)
df_2013=pd.read_csv('./forbes_2013.csv',encoding='gbk',thousands=',')
print('type of dataframe', df_2013.shape)
print(df_2013.dtypes)
df_2013.head(3)

column_update = ['Rank', 'Company_en', 'Country_en', 'Sales', 'Profits', 'Assets', 'Market_value']
df_2013.columns = column_update
#df_2013[df_2013['Sales'].str.contains('.*[A-Za-z]', regex=True)]

df_2013['Assets']=df_2013['Assets'].replace(',','',regex=True)
df_2013[pd.isnull(df_2013['Profits'])]
df_2013['Profits'].ffill(0,inplace=True)
# df_2013['Assets']=pd.to_numeric(df_2013['Assets'])
# df_2013['Profits']=pd.to_numeric(df_2013['Profits'])
# df_2013['Sales']=pd.to_numeric(df_2013['Sales'])
df_2013['Country_en']=df_2013['Country_en'].replace(['HK.*','TA'],['CN-HK','CN-TA'],regex=True)
df_2013[['Sales','Profits','Assets','Market_value']]=df_2013[['Sales','Profits','Assets'
    ,'Market_value']].apply(lambda x:x/10)
df_2013['Year']=2013
df_2013['Country_cn_en'],df_2013['Industry_cn'],df_2013['Industry_en']=['','','']
print(df_2013)

column_sort=['Rank', 'Company_en', 'Country_en', 'Sales', 'Profits', 'Assets', 'Market_value']
df_2013=df_2013.reindex(columns=column_sort)


print(df_2013.shape)
print(df_2013.dtypes)

