import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from IPython.core.pylabtools import figsize
from  matplotlib import cm

plt.style.use('ggplot')
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

zhilian_db = pd.read_csv("./zhilian.csv", encoding='gbk')

print('行数为{}'.format(zhilian_db.shape[0]))

zhilian_db['save_date'] = pd.to_datetime(zhilian_db['save_date'])

print(zhilian_db['save_date'].dtype)

zhilian_db = zhilian_db[zhilian_db['zwyx'].str.contains('\d+-\d+', regex=True)]

print('行数为{}'.format(zhilian_db.shape[0]))

# 将工资字段截取为最大和最小
s_min, s_max = zhilian_db.loc[:, 'zwyx'].str.split('-', 1).str

df_min = pd.DataFrame(s_min)
df_min.columns = ['zwyx_min']
df_max = pd.DataFrame(s_max)
df_max.columns = ['zwyx_max']

zhilian_db_concat = pd.concat([zhilian_db, df_min, df_max], axis=1)

zhilian_db_concat['zwyx_min'] = pd.to_numeric(zhilian_db_concat['zwyx_min'])
zhilian_db_concat['zwyx_max'] = pd.to_numeric(zhilian_db_concat['zwyx_max'])

print(zhilian_db_concat.dtypes)

print(zhilian_db_concat.head(2))

zhilian_db_concat.sort_values('zwyx_min', inplace=True)

# 根据链接判断是否有重复数据
# print(zhilian_db_concat[zhilian_db_concat.duplicated('zw_link')==True])

# --------------工作分布-----------------
ADDRESS = ['北京', '上海', '广州', '深圳',
           '天津', '武汉', '西安', '成都', '大连',
           '长春', '沈阳', '南京', '济南', '青岛',
           '杭州', '苏州', '无锡', '宁波', '重庆',
           '郑州', '长沙', '福州', '厦门', '哈尔滨',
           '石家庄', '合肥', '惠州', '太原', '昆明',
           '烟台', '佛山', '南昌', '贵阳', '南宁']

df_city = zhilian_db_concat.copy()

for city in ADDRESS:
    city_regx = city + '.*'
    df_city['gzdd'] = df_city['gzdd'].replace([city_regx], [city], regex=True)

df_city_main = df_city[df_city['gzdd'].isin(ADDRESS)]

df_city_main_count = df_city_main.groupby('gzdd')['zwmc', 'gsmc'].count()

df_city_main_count['gsmc'] = df_city_main_count['gsmc'] / (df_city_main_count['gsmc'].sum())

df_city_main_count.columns = ['number', 'percentage']

df_city_main_count.sort_values(by='number', ascending=False, inplace=True)

df_city_main_count['label'] = df_city_main_count.index + ' ' + (
((df_city_main_count['percentage']) * 100)
.round()).astype('int').astype('str') + '%'

print(df_city_main_count.head(10))

label = df_city_main_count['label']
sizes = df_city_main_count['number']

# fig, axes = plt.subplots(figsize=(10, 6), ncols=2)
# ax1, ax2 = axes.ravel()
#
# colors = cm.PiYG(np.arange(len(sizes)) / len(sizes))
#
# patches, texts = ax1.pie(sizes, labels=None, shadow=False, startangle=0, colors=colors)
# ax1.axis('equal')
# ax1.set_title('职位数量分布', loc='center')
#
# ax2.axis('off')
# ax2.legend(patches, label, loc='center left', fontsize=9)
# plt.savefig('job_distribute.png')
# plt.show()
# --------------工作分布完-----------------

# 月薪分布情况
from matplotlib.ticker import  FormatStrFormatter

fig,(ax3,ax4)=plt.subplots(figsize=(10,8),nrows=2)
print(zhilian_db_concat.shape[1])
x_pos=list(range(zhilian_db_concat.shape[0]))
y1=zhilian_db_concat['zwyx_min']
ax3.plot(x_pos,y1)
ax3.set_title('中国每月最低工资分布',size=14)
ax3.set_xticklabels('')
ax3.set_ylabel('最低工资')
bins = [3000,6000, 9000, 12000, 15000, 18000, 21000, 24000, 100000]
print(bins[:-1])
counts,bins,patches=ax4.hist(y1,bins,histtype='bar',facecolor='g',rwidth=0.8)
ax4.set_title=('中国每月最低工资分布柱状图')
ax4.set_xticks(bins)
ax4.set_xticklabels(bins,rotation=90)
bin_centers=0.5*np.diff(bins)+bins[:-1]
for count,x in zip(counts,bin_centers):
    percent='%0.0f%%'%(100 * float(count)/counts.sum())
    ax4.annotate(percent,xy=(x,0),xycoords=('data','axes fraction'),
    xytext=(0,-40),textcoords='offset points',va='top',ha='center'
    ,rotation=-90,color='b',size=14)
plt.show()