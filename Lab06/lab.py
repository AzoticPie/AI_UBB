import pandas as pd
import os
import numpy as np  
from sklearn import linear_model
from sklearn.metrics import mean_squared_error as mse
import plot
import utils
import my_regression

crt_dir =  os.getcwd()
file_path = os.path.join(crt_dir, 'data', 'v3_world_happiness-report-2017.csv')

df = pd.read_csv(file_path)
input_labels = ['Freedom', 'Economy..GDP.per.Capita.']
output_label = 'Happiness.Score'


df_train, df_validate = utils.separate_data_df_lipsa(df, input_labels, input_labels[0])


x = df_train.drop(input_labels[0], axis=1)
y = df_train[input_labels[0]]

# sklearn
regressor = linear_model.LinearRegression()
regressor.fit(x, y)

w0, w1, w2 = regressor.intercept_, regressor.coef_[0], 0
print('the learnt model: f(x) = ', w0, ' + ', w1, ' * x1 + ', w2 , '* x2')

print(df_validate)
df_val = df_validate.drop(input_labels[0], axis=1)
df_validate['predicted'] = regressor.predict(df_val)
print(df_validate)