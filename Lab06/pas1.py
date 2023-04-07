import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np  
from sklearn import linear_model

crtDir =  os.getcwd()
filePath = os.path.join(crtDir, 'data', 'v1_world_happiness-report-2017.csv')

df = pd.read_csv(filePath)

print(df[["Happiness.Score", "Economy..GDP.per.Capita."]].head(20))
