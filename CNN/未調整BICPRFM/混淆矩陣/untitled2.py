# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 02:34:53 2019

@author: user
"""

import pandas as pd
import numpy as np


df = pd.read_csv('f3.csv',header = None)
df = np.array(df)
print(df[0][0] == 0)
#data = df.iloc[0:1,0:12]
#i=1
#new = pd.DataFrame()
a=[]
for i in range(127):
    for j in range(12):
        if(df[i][j] == 0):
            a.append("False")
        else: 
            if(df[i][j] == 1):
                a.append("True") 

print(a)
a=pd.DataFrame(a)
a.to_csv("finally.csv",mode='w', header=False,index=False) 

