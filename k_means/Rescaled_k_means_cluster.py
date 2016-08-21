# -*- coding: utf-8 -*-
"""
Created on Sat Jul 30 09:44:17 2016

@author: yuchengtsai
"""

import pickle
from sklearn.preprocessing import MinMaxScaler
import numpy

data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
### there's an outlier--remove it! 
data_dict.pop("TOTAL", 0)

feature_1 = "salary"
feature_2 = "exercised_stock_options"

salary =[]
ex_stock =[]

for users in data_dict:
    val = data_dict[users]['salary']
    if val =='NaN':
        continue
    salary.append(float(val))
    val = data_dict[users]['exercised_stock_options']
    if val =='NaN':
        continue
    ex_stock.append(float(val))

salary = [min(salary),200000,max(salary)]
ex_stock =[min(ex_stock),1000000,max(ex_stock)]

print salary
print ex_stock

scaler_salary = MinMaxScaler()
scaler_stock = MinMaxScaler()

rescaled_salary = scaler_salary.fit_transform(salary)
rescaled_stock = scaler_salary.fit_transform(ex_stock)

print rescaled_salary
print rescaled_stock
    