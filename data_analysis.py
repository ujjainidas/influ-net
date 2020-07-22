# -*- coding: utf-8 -*-
"""
@author: Ujjaini Das
"""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

flu_data = pd.read_csv('flu_data_cleaned.csv')

descriptive_stats = flu_data.describe()
#descriptive_stats.to_csv(r'C:\Users\thisi\Desktop\Machine Learning\influ-net-linkedin-mentorship\descriptive_stats.csv')

#plt.scatter(flu_data['REGION'], flu_data['% WEIGHTED ILI'])
#plt.scatter(flu_data['REGION'], flu_data['%UNWEIGHTED ILI'])
#plt.scatter(flu_data['REGION'], flu_data['%UNWEIGHTED ILI'])
plt.scatter(flu_data['WEEK'], flu_data['AGE 0-4']) #blue
plt.scatter(flu_data['WEEK'], flu_data['AGE 25-49']) #orange
plt.scatter(flu_data['WEEK'], flu_data['AGE 5-24']) #green
plt.scatter(flu_data['WEEK'], flu_data['AGE 50-64']) #red
plt.scatter(flu_data['WEEK'], flu_data['AGE 65']) #purple
plt.show()

corrmat = flu_data.corr()
f = sns.heatmap(corrmat, vmax=.8, square=True, annot=True, cbar=False)
