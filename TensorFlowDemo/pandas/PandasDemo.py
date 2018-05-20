import pandas as pd
import matplotlib.pyplot as plt


city_names=pd.Series(['chengdu','beijing','shanghai'])
population=pd.Series([50000000,100000,20000])
china_dataframe=pd.DataFrame({'citynames':city_names,'population':population})
china_dataframe['Area square miles'] = pd.Series([51, 176.53, 97.92])
china_dataframe['Population density'] = china_dataframe['population'] / china_dataframe['Area square miles']
china_dataframe['is wide and has c']=(china_dataframe['Area square miles'] > 50) & china_dataframe['citynames'].apply(lambda name: name.startswith('c'))
print(china_dataframe)
# california_housing_dataframe = pd.read_csv("C:\\Users\\menglihuan\\Desktop\\california_housing_train .csv", sep=",")
# california_housing_dataframe.describe()
# plt.show()
# california_housing_dataframe.head()
# plt.show()
# california_housing_dataframe.hist('housing_median_age')
# plt.show()
