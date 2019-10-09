# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 10:49:06 2019

@author: user
"""

import csv
import pandas as pd
import numpy as np
import random

df = pd.read_csv('a.csv')
#data = df.iloc[0:2,0:2]

#select = random.randint(0,10)
#print(data)
#print(select)

for i in range(3):
    select = random.randint(0,10)
    data = df.iloc[select:select+1]
    data2 = df.iloc[select+1:select+2]
#    data3 = (data.value+data2.value)/2
    data3 = pd.DataFrame((data.values + data2.values)/2, columns=data.columns)
#    print(data)
    print(data3)
    print(data)
    print(data2)
    data3.to_csv("a.csv",mode='a', header=False,index=False)    
    
    
  