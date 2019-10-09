# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 01:55:10 2019

@author: user
"""
import pandas as pd


df = pd.read_csv('t.csv')
dft = df["ALL"].str.split(' ',expand = True)
print(dft)
dft.to_csv("f.csv",mode='w', header=False,index=False) 
