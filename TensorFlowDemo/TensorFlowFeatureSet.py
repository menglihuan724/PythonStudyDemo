import math

from matplotlib import cm
from matplotlib import gridspec
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
from sklearn import metrics
import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow.python.data import Dataset

tf.logging.set_verbosity(tf.logging.ERROR)
pd.options.display.max_rows = 10
pd.options.display.float_format = '{:.1f}'.format
california_housing_dataframe = pd.read_csv('D:\myproject\PythonStudyDemo\TensorFlowDemo\california_housing_train .csv',
                                           sep=",")
california_housing_dataframe = california_housing_dataframe.reindex(
    np.random.permutation(california_housing_dataframe.index))


# 准备数据
def processFeatures(california_housing_dataframe):
    selected_features = california_housing_dataframe[
        ["latitude",
         "longitude",
         "housing_median_age",
         "total_rooms",
         "total_bedrooms",
         "population",
         "households",
         "median_income"]]
    processed_features = selected_features.copy()
    processed_features["room_per_person"] = (processed_features["total_rooms"] / processed_features["population"])
    return processed_features


def preTargets(california_housing_dataframe):
    out_targets = pd.DataFrame()
    out_targets["median_house_value"] = (california_housing_dataframe["median_house_value"] / 1000)
    return out_targets


# 打印数据
train_example = processFeatures(california_housing_dataframe.head(12000))
train_target = preTargets(california_housing_dataframe.head(12000))

validtion_example = processFeatures(california_housing_dataframe.head(5000))
validtion_target = preTargets(california_housing_dataframe.head(5000))

print("训练数据特征:")
print(train_example)
print("训练数据目标")
print(train_target)

print("验证数据特征:")
print(validtion_example)
print("验证数据目标")
print(validtion_target)


def get_quantile_based_boundaries(features_values, num_buckets):
    boundaries = np.arange(1.0, num_buckets) / num_buckets
    quantiles = features_values.quantile(boundaries)
    return [quantiles[q] for q in quantiles.keys()]


# def construct_feature_columns(input_features):
#     return set([tf.feature_column.numeric_column(myfeatures) for myfeatures in input_features])
# 分桶模型
def construct_feature_columns():
    households = tf.feature_column.numeric_column("households")
    longitude = tf.feature_column.numeric_column("longitude")
    latitude = tf.feature_column.numeric_column("latitude")
    housing_median_age = tf.feature_column.numeric_column("housing_median_age")
    median_income = tf.feature_column.numeric_column("median_income")
    rooms_per_person = tf.feature_column.numeric_column("room_per_person")

    bucketized_households = tf.feature_column.bucketized_column(households, boundaries=get_quantile_based_boundaries(
        train_example["households"], 7))
    bucketized_longitude = tf.feature_column.bucketized_column(longitude, boundaries=get_quantile_based_boundaries(
        train_example["longitude"], 10))
    bucketized_latitude = tf.feature_column.bucketized_column(latitude, boundaries=get_quantile_based_boundaries(
        train_example["latitude"], 10))
    bucketized_housing_median_age = tf.feature_column.bucketized_column(housing_median_age,
                                                                        boundaries=get_quantile_based_boundaries(
                                                                            train_example["housing_median_age"], 7))
    bucketized_median_income = tf.feature_column.bucketized_column(median_income,
                                                                   boundaries=get_quantile_based_boundaries(
                                                                       train_example["median_income"], 7))
    bucketized_rooms_per_person = tf.feature_column.bucketized_column(rooms_per_person,
                                                                      boundaries=get_quantile_based_boundaries(
                                                                          train_example["room_per_person"], 7))
    latitude_longtiude = tf.feature_column.crossed_column(set([bucketized_latitude, bucketized_longitude]),
                                                          hash_bucket_size=2400)

    features_col = set([bucketized_households,
                        bucketized_longitude,
                        bucketized_latitude,
                        bucketized_housing_median_age,
                        bucketized_median_income,
                        bucketized_rooms_per_person,
                        latitude_longtiude
                        ])

    return features_col


def my_input_fn(features, targets, batch_size=1, shuffle=True, num_epochs=None):
    features = {key: np.array(value) for key, value in dict(features).items()}
    dataSet = Dataset.from_tensor_slices((features, targets))
    dataSet = dataSet.batch(batch_size).repeat(num_epochs)
    if shuffle:
        dataSet = dataSet.shuffle(1000)
    features, lables = dataSet.make_one_shot_iterator().get_next()
    return features, lables


def train(rate, steps, feature_columns, batch_size, train_examples, train_targets, validtion_examples,
          validtion_targets):
    periods = 10
    steps_per_period = steps / periods

    # my_optimizer = tf.train.GradientDescentOptimizer(learning_rate=rate)
    # 换成FTRL优化算法
    my_optimizer = tf.train.FtrlOptimizer(learning_rate=rate)
    my_optimizer = tf.contrib.estimator.clip_gradients_by_norm(my_optimizer, 5.0)
    linear_regressor = tf.estimator.LinearRegressor(
        feature_columns=feature_columns,
        optimizer=my_optimizer
    )
    train_input_fn = lambda: my_input_fn(train_examples, train_targets["median_house_value"], batch_size=batch_size)
    predTrain_fn = lambda: my_input_fn(train_examples, train_targets["median_house_value"], num_epochs=1, shuffle=False)
    predValtion_fn = lambda: my_input_fn(validtion_examples, validtion_targets["median_house_value"], num_epochs=1,
                                         shuffle=False)
    print("开始训练")
    print('RMSE')
    train_rmse = []
    vald_rmse = []
    for period in range(0, periods):
        linear_regressor.train(
            input_fn=train_input_fn,
            steps=steps_per_period,
        )
        train_predictions = linear_regressor.predict(input_fn=predTrain_fn)
        train_predictions = np.array([item['predictions'][0] for item in train_predictions])

        validation_predictions = linear_regressor.predict(input_fn=predValtion_fn)
        validation_predictions = np.array([item['predictions'][0] for item in validation_predictions])

        training_root_mean_squared_error = math.sqrt(
            metrics.mean_squared_error(train_predictions, train_targets))
        validation_root_mean_squared_error = math.sqrt(
            metrics.mean_squared_error(validation_predictions, validtion_targets))
        print("  周期 %02d : %0.2f" % (period, training_root_mean_squared_error))
        train_rmse.append(training_root_mean_squared_error)
        vald_rmse.append(validation_root_mean_squared_error)
    print("模型训练结束")

    plt.ylabel("RMSE")
    plt.xlabel("周期")
    plt.title("均方根误差 vs. 周期")
    plt.tight_layout()
    plt.plot(train_rmse, label="training")
    plt.plot(vald_rmse, label="validation")
    plt.legend()
    plt.show()
    return linear_regressor


minimal_features = [
    "latitude",
    "longitude",
    "housing_median_age",
    "total_rooms",
    "total_bedrooms",
    "population",
    "households",
    "median_income",
    "room_per_person"
]

assert minimal_features, "You must select at least one feature!"

minimal_training_examples = train_example[minimal_features]
minimal_validation_examples = validtion_example[minimal_features]

train(
    rate=5,
    steps=500,
    batch_size=100,
    feature_columns=construct_feature_columns(),
    train_examples=minimal_training_examples,
    train_targets=train_target,
    validtion_examples=minimal_validation_examples,
    validtion_targets=validtion_target)

LATITUDE_RANGES = zip(range(32, 44), range(33, 45))


def select_and_transform_features(source_df):
    selected_examples = pd.DataFrame()
    selected_examples["median_income"] = source_df["median_income"]
    for r in LATITUDE_RANGES:
        selected_examples["latitude_%d_to_%d" % r] = source_df["latitude"].apply(
            lambda l: 1.0 if l >= r[0] and l < r[1] else 0.0)
    return selected_examples


selected_training_examples = select_and_transform_features(train_example)
selected_validation_examples = select_and_transform_features(validtion_example)

# _ = train(
#     rate=1,
#     steps=500,
#     batch_size=100,
#     train_examples=selected_training_examples,
#     train_targets=train_target,
#     validtion_examples=selected_validation_examples,
#     validtion_targets=validtion_target)
