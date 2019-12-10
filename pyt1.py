a#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 20:13:45 2018
@author: alan
"""
import os
print(os.getcwd())
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
#from matplotlib import style
#style.use('ggplot')
passmark = 40
df = pd.read_csv("/home/alan/Python/StudentsPerformance.csv")
print(df.head())

print (df.shape)
df.describe()
df.isnull().sum()
sns.countplot(x="math score", data = df, palette="muted")
plt.show()

df['Math_PassStatus'] = np.where(df['math score']<passmark, 'F', 'P')
df.Math_PassStatus.value_counts()
sns.countplot(x='parental level of education', data = df, hue='Math_PassStatus', palette='bright')
plt.show()
sns.countplot(x="reading score", data = df, palette="muted")
plt.show()
df['Reading_PassStatus'] = np.where(df['reading score']<passmark, 'F', 'P')
df.Reading_PassStatus.value_counts()
sns.countplot(x='parental level of education', data = df, hue='Reading_PassStatus', palette='bright')
plt.show()
sns.countplot(x="writing score", data = df, palette="muted")
plt.show()
df['Writing_PassStatus'] = np.where(df['writing score']<passmark, 'F', 'P')
df.Writing_PassStatus.value_counts()
sns.countplot(x='parental level of education', data = df, hue='Writing_PassStatus', palette='bright')
plt.show()

df['OverAll_PassStatus'] = df.apply(lambda x : 'F' if x['Math_PassStatus'] == 'F' or 
                                    x['Reading_PassStatus'] == 'F' or x['Writing_PassStatus'] == 'F' else 'P', axis =1)

df.OverAll_PassStatus.value_counts()
sns.countplot(x='parental level of education', data = df, hue='OverAll_PassStatus', palette='bright')
plt.show()

df['Total_Marks'] = df['math score']+df['reading score']+df['writing score']
df['Percentage'] = df['Total_Marks']/3

sns.countplot(x="Percentage", data = df, palette="muted")
plt.show()

def GetGrade(Percentage, OverAll_PassStatus):
    if ( OverAll_PassStatus == 'F'):
        return 'F'    
    if ( Percentage >= 80 ):
        return 'A'
    if ( Percentage >= 70):
        return 'B'
    if ( Percentage >= 60):
        return 'C'
    if ( Percentage >= 50):
        return 'D'
    if ( Percentage >= 40):
        return 'E'
    else: 
        return 'F'

df['Grade'] = df.apply(lambda x : GetGrade(x['Percentage'], x['OverAll_PassStatus']), axis=1)

df.Grade.value_counts()
sns.countplot(x="Grade", data = df, order=['A','B','C','D','E','F'],  palette="muted")
plt.show()

sns.countplot(x='parental level of education', data = df, hue='Grade', palette='bright')
plt.show()
