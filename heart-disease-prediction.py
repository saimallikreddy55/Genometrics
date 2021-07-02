# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 12:17:41 2021

@author: jsmur
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import joblib

heart_data = pd.read_csv('C:/Users/91970/projects/genometrics/heart.csv')
print("First rows of data:" ,heart_data.head())
print()
print("Shape of data:" ,heart_data.shape)
print("Information: ",heart_data.info())
print("Checking for null values:", heart_data.isnull().sum())
print("Finding the measures of data: ",heart_data.describe())

#1 =  Unhealthy Heart
#0 =  Healthy Heart
# IN TAGRET COLUMN 0,1 REPRESENT ABOVE VALUES. 
print()
print("Target value counts: ")
print(heart_data['target'].value_counts())

print()
# processing of data
x = heart_data.drop(columns='target', axis=1) #column axis =1, row axis=0
y = heart_data['target']
print("PROCESSING OF DATA, X AND Y COLUMNS: ")
print(x)
print()
print(y)

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2,stratify=y, random_state=3)

print("X DATA: ", x.shape, x_train.shape, x_test.shape)
print("Y DATA: ", y.shape, y_train.shape, y_test.shape)
print()
print()

print("TRANINING OF DATA ")
print()

model = LogisticRegression(solver='lbfgs', max_iter=1000, random_state=0)
model.fit(x_train,y_train)

#To dumb the trained model into a pickel file 

filename= 'heartSaved_model.sav'
saved_model=joblib.dump(model,filename)


