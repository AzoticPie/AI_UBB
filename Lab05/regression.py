import pandas as pd
from math import sqrt
import matplotlib.pyplot as plt

#read csv
df = pd.read_csv('data\\sport.csv')

#calculate differences between real and predicted values 

df['weight_diff_abs'] = df.apply(lambda row: abs(row['Weight'] - row['PredictedWeight']), axis=1)
df['weight_diff_squared'] = df.apply(lambda row: (row['Weight'] - row['PredictedWeight'])**2, axis=1)


df['waist_diff_abs'] = df.apply(lambda row: abs(row['Waist'] - row['PredictedWaist']), axis=1)
df['waist_diff_squared'] = df.apply(lambda row: (row['Waist'] - row['PredictedWaist'])**2, axis=1)

df['pulse_diff_abs'] = df.apply(lambda row: abs(row['Pulse'] - row['PredictedPulse']), axis=1)
df['pulse_diff_squared'] = df.apply(lambda row: (row['Pulse'] - row['PredictedPulse'])**2, axis=1)


#calculate weight error
WeightMAE = df['weight_diff_abs'].sum()/df.shape[0]
WeightRMSE = sqrt(df['weight_diff_squared'].sum()/df.shape[0])

WaistMAE = df['waist_diff_abs'].sum()/df.shape[0]
WaistRMSE = sqrt(df['waist_diff_squared'].sum()/df.shape[0])

PulseMAE = df['pulse_diff_abs'].sum()/df.shape[0]
PulseRMSE = sqrt(df['pulse_diff_squared'].sum()/df.shape[0])

#plot
df_weight_plot = df[['Weight', 'PredictedWeight']]
df_waist_plot = df[['Waist', 'PredictedWaist']]
df_pulse_plot = df[['Pulse', 'PredictedPulse']]

fig, axs = plt.subplots(ncols=3, figsize=(15, 8))

title_1 = f'Weight MAE = {WeightMAE:.3f}\nWeight RMSE = {WeightRMSE:.3f}'
title_2 = f'Waist MAE = {WaistMAE:.3f}\nWaist RMSE = {WaistRMSE:.3f}'
title_3 = f'Pulse MAE = {PulseMAE:.3f}\nPulse RMSE = {PulseRMSE:.3f}'

df_weight_plot.plot(y=['Weight', 'PredictedWeight'], kind='bar', ax=axs[0], title=title_1)
df_waist_plot.plot(y=['Waist', 'PredictedWaist'], kind='bar', ax=axs[1], title=title_2)
df_pulse_plot.plot(y=['Pulse', 'PredictedPulse'], kind='bar', ax=axs[2], title=title_3)

fig.suptitle('Model Predictions vs Actual Measurements')
plt.show()