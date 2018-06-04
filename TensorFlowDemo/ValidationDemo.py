import math
from IPython import display
from matplotlib import cm
from matplotlib import gridspec
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
from sklearn import metrics
import tensorflow as tf
from tensorflow.python.data import Dataset

pd.__version__
tf.logging.set_verbosity(tf.logging.ERROR)
pd.options.display.max_rows=10
pd.options.display.float_format='{:.1f}'.format
#导入数据
housing_dataframe=pd.read_csv("C:\\Users\\terrymeng\\Desktop\\data\\california_housing_train.csv", sep=",")

def preprocess_features(housingDataframe):
    #纬度，经度，住房中位数年龄
    select_features=housingDataframe[["latitude",
                                      "longitude",
                                      "housing_median_age",
                                      "total_rooms",
                                      "total_bedrooms",
                                      "population",
                                      "households",
                                      "median_income"]]
    process_features=select_features.copy()
    process_features["room_per_persons"]=(housingDataframe["total_rooms"]/housingDataframe["population"])
    return process_features

def preprocess_target(housingDataframe):
    target=pd.DataFrame()
    target["median_house_value"]=(housingDataframe["median_house_value"]/1000)
    return target
#训练集12000
training_examples = preprocess_features(housing_dataframe.head(12000))
training_examples.describe()
training_targets = preprocess_target(housing_dataframe.head(12000))
training_targets.describe()

#验证集5000
validation_examples = preprocess_features(housing_dataframe.tail(5000))
validation_examples.describe()

validation_targets = preprocess_target(housing_dataframe.tail(5000))
validation_targets.describe()


#绘图
plt.figure(figsize=(13, 8))
ax = plt.subplot(1, 2, 1)
ax.set_title("Validation Data")

ax.set_autoscaley_on(True)
ax.set_ylim([32, 43])
ax.set_autoscalex_on(True)
ax.set_xlim([-126, -112])
plt.scatter(validation_examples["longitude"],
            validation_examples["latitude"],
            cmap="coolwarm",
            c=validation_targets["median_house_value"] / validation_targets["median_house_value"].max())

ax = plt.subplot(1,2,2)
ax.set_title("Training Data")

ax.set_autoscaley_on(False)
ax.set_ylim([32, 43])
ax.set_autoscalex_on(False)
ax.set_xlim([-126, -112])
plt.scatter(training_examples["longitude"],
            training_examples["latitude"],
            cmap="coolwarm",
            c=training_targets["median_house_value"] / training_targets["median_house_value"].max())
_ = plt.plot()
# plt.show()

#模型训练
def input_fn(features,targets,batch_size=5,shuffle=True,num_epochs=None):
    features={key:np.array(value) for key,value in dict(features).items()}
    ds=Dataset.from_tensor_slices(features)
    ds=ds.batch(batch_size).repeat(num_epochs)
    if shuffle:
        ds=ds.shuffle(10000)
    features,lables=ds.make_one_shot_iterator().next()
    return features,lables
def construct_features_col(input_features):
    return set([tf.feature_column.numeric_column(myfeatrues) for myfeatrues in input_features])
def train_model(
        learning_rate,
        steps,
        batch_size,
        training_examples,
        training_targets,
        validation_examples,
        validation_targets):
    peroids=10
    steps_per_peroids=steps/peroids
    my_optimizer = tf.train.GradientDescentOptimizer(learning_rate=learning_rate)
    my_optimizer = tf.contrib.estimator.clip_gradients_by_norm(my_optimizer, 5.0)
    linear_regressor = tf.estimator.LinearRegressor(
        feature_columns=construct_features_col(training_examples),
        optimizer=my_optimizer
    )
    trainning_input_fn=lambda:input_fn(training_examples,
                                        training_targets,
                                        training_targets["median_house_value"]
                                       )
    predict_training_input_fn=lambda:input_fn(validation_examples,
                                               validation_targets,
                                               validation_targets["median_houst_value"],num_epochs=1,shuffle=False)

    prdeict_validation_input_fn=lambda:input_fn(validation_examples,validation_targets["median_house_value"]
                                                 ,num_epochs=1,shuffle=False)
    print("Training model...")
    print("RMSE (on training data):")
    training_rmse = []
    validation_rmse = []
    for period in range (0, peroids):
        linear_regressor.train(
            input_fn=trainning_input_fn,
            steps=steps_per_peroids
        )
        train_predictions=linear_regressor.predict(input_fn=predict_training_input_fn)
        training_predictions=np.array([item['predictions'][0] for item in train_predictions])
        validation_predictions=linear_regressor.predict(input_fn=prdeict_validation_input_fn)
        validation_predictions=linear_regressor.predict([item["predictions"][0]for item in validation_predictions])
        training_root_mean_squared_error = math.sqrt(
        metrics.mean_squared_error(training_predictions, training_targets))
        validation_root_mean_squared_error = math.sqrt(
        metrics.mean_squared_error(validation_predictions, validation_targets))
        print ("  period %02d : %0.2f" % (period, training_root_mean_squared_error))
        training_rmse.append(training_root_mean_squared_error)
        validation_rmse.append(validation_root_mean_squared_error)
    print("Model training finished.")
    plt.ylabel("RMSE")
    plt.xlabel("Periods")
    plt.title("Root Mean Squared Error vs. Periods")
    plt.tight_layout()
    plt.plot(training_rmse, label="training")
    plt.plot(validation_rmse, label="validation")
    plt.legend()
    return linear_regressor

#test
linear_regressor = train_model(
    learning_rate=0.00003,
    steps=500,
    batch_size=5,
    training_examples=training_examples,
    training_targets=training_targets,
    validation_examples=validation_examples,
    validation_targets=validation_targets)