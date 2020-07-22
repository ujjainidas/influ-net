# -*- coding: utf-8 -*-
"""
@author: Ujjaini Das
"""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
    
def find_avg(cols_list, index):
    sum = 0
    count = 5
    for cols in cols_list:
        if cols[index] != 'X':
            sum = sum + cols[index]
        else:
            count = count - 1
    return sum/count
    
flu_data = pd.read_csv('ILINet.csv')
col0 = flu_data["AGE 0-4"]
col25 = flu_data["AGE 25-49"]
col5 = flu_data["AGE 5-24"]
col50 = flu_data["AGE 50-64"]
col65 = flu_data["AGE 65"]
cols_list = [col0, col5, col25, col50, col65]


for col in cols_list:
    for index in range(len(col)):
       if col[index] == 'X':
           col[index] = find_avg(cols_list, index)

col_regions = flu_data["REGION"]
for index in range(len(col_regions)):
    if col_regions[index] == "New England":
        col_regions[index] = 0
    elif col_regions[index] == "Mid-Atlantic":
        col_regions[index] = 1
    elif col_regions[index] == "East North Central":
        col_regions[index] = 2
    elif col_regions[index] == "West North Central":
        col_regions[index] = 3
    elif col_regions[index] == "South Atlantic":
        col_regions[index] = 4
    elif col_regions[index] == "East South Central":
        col_regions[index] = 5
    elif col_regions[index] == "West South Central":
        col_regions[index] = 6
    elif col_regions[index] == "Mountain":
        col_regions[index] = 7
    elif col_regions[index] == "Pacific":
        col_regions[index] = 8

flu_data["AGE 0-4"] = col0
flu_data["AGE 5-24"] = col5
flu_data["AGE 25-49"] = col25
flu_data["AGE 50-64"] = col50
flu_data["AGE 65"] = col65
flu_data["REGION"] = col_regions

flu_data.to_csv(r'C:\Users\thisi\Desktop\Machine Learning\influ-net-linkedin-mentorship\flu_data_cleaned.csv')