#!/usr/bin/python
#coding:utf8

import pandas as pd
import tensorflow as tf
import numpy as np
tf.logging.set_verbosity(tf.logging.ERROR)
pd.options.display.max_rows = 10
pd.options.display.float_format = "{:.1f}".format
#显示所有行
#显示所有列
pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", None)

california_housing_dataframe = pd.read_csv("../california_housing_train.csv")
california_housing_dataframe.reindex(
    np.random.permutation(california_housing_dataframe.index))
california_housing_dataframe["median_house_value"]/=10
print(california_housing_dataframe.describe())

#定义特征行,总房间数
my_feature=california_housing_dataframe[["total_rooms"]]
feature_colums=[tf.feature_column.numeric_column("total_rooms")]
print(my_feature['total_rooms'][[0,1,2,3]])
print(my_feature['total_rooms']+my_feature['total_rooms'][[0,1,2,3]])


