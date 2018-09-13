#!/usr/bin/python
#coding:utf8
import math
import pandas as pd
import tensorflow as tf
import numpy as np
from sklearn import metrics
from tensorflow.python.data import Dataset

line='-'*10
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
feature_columns=[tf.feature_column.numeric_column("total_rooms")]
# print(my_feature['total_rooms'][[0,1,2,3]])
# print(my_feature['total_rooms']+my_feature['total_rooms'][[0,1,2,3]])
#目标
targets = california_housing_dataframe["median_house_value"]
#
my_optimizer=tf.train.GradientDescentOptimizer(learning_rate=0.0000001)
my_optimizer=tf.contrib.estimator.clip_gradients_by_norm(my_optimizer,5.0)
linear_regressor=tf.estimator.LinearRegressor(feature_columns=feature_columns,optimizer=my_optimizer)
#输入函数
def my_input_fn(features,targets,batch_size=1,shuffle=True,num_epochs=True):
    features={key:np.array(value)for key,value in dict(features).items()}
    print(features)
    ds=Dataset.from_tensor_slices((features,targets))
    ds=ds.batch(batch_size).repeat(num_epochs)
    if shuffle:
        ds=ds.shuffle(buffer_size=1000)
    features,labels=ds.make_one_shot_iterator().get_next()
    return features,labels

#训练
_ = linear_regressor.train(
    input_fn = lambda:my_input_fn(my_feature, targets),
    steps=100
)
#预测
prediction_input_fn =lambda: my_input_fn(my_feature, targets, num_epochs=1, shuffle=False)

predictions = linear_regressor.predict(input_fn=prediction_input_fn)
predictions = np.array([item['predictions'][0] for item in predictions])
mean_squared_error = metrics.mean_squared_error(predictions, targets)
root_mean_squared_error = math.sqrt(mean_squared_error)
print("Mean Squared Error (on training data): %0.3f" % mean_squared_error)
print("Root Mean Squared Error (on training data): %0.3f" % root_mean_squared_error)

#对比误差
check_data=pd.DataFrame()
check_data["predictions"]=pd.Series(predictions)
check_data["targets"]=pd.Series(targets)
print(f'对比数据{check_data.describe()}')