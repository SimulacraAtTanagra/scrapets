# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 12:13:14 2020

@author: shane
"""
from admin import newest, colclean
import pandas as pd
import numpy as np

#this is for collecting the metadata necessary to complete the 

path='c://users//shane//downloads//'
fname='Crystal'
df=colclean(pd.read_excel(newest(path,fname)))
df=df[['ssn', 'name', '9', '10', '11', '12', '13', '14', '15',
       '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27',
       '28']]

#replacing zeros with null fields
for i in df.columns[2:]:
    df[i]=df[i].replace(to_replace={0:np.nan})

newlist=[]
for i in df.ssn.unique():
    x= list(df.loc[df['ssn'] == i].dropna(axis=1).columns[2:])
    newlist.append((str(i),x))
    
