# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 09:28:07 2020

@author: USER
"""


import numpy as np
import pandas as pd

arr_pand = np.random.randint(0,10,6).reshape(2,3)

df1 = pd.DataFrame(arr_pand)

s1 = df1[0]

s2 = df1[1]

s3 = df1[2]

#Operacion con la serie

print(arr_pand * 2)

df1[3] = s1

df1[4] = s1 *s2

print(df1[2][0])


datos_fisicos_uno = pd.DataFrame(
    arr_pand,
    columns =[
        'Estatura (cm)',
        'Peso (kg)',
        'Edad (anios)'
        ])

datos_fisicos_dos = pd.DataFrame(
    arr_pand,
    columns =[
        'Estatura (cm)',
        'Peso (kg)',
        'Edad (anios)'
        ],
    index = {
        'Adrain',
        'Vicente'})

df1.index = ["Adrain",'Vicente']
df1.index = ["Wendy",'Carolina']

df1.columns = ['A','B','C','D','E']
