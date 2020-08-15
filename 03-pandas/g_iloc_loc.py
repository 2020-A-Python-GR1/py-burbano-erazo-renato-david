# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 07:58:18 2020

@author: USER
"""

import pandas as pd

path = "C://GitKraken_Repositorios//py-burbano-erazo-renato-david//03-pandas//data//artwork_data.csv"

df = pd.read_csv(path)

# loc ---> Obtener un registro, filtrado horizontal

filtrado_horizontal = df.loc[1035] # Serie,    Filtrar por indice (1)
print(filtrado_horizontal)
print(filtrado_horizontal['artist'])
print(filtrado_horizontal.index)


serie_vertical = df['artist']
print(serie_vertical)
print(serie_vertical.index)


#Filtrado por indice
df_1035 = df[df.index == 1035]


#loc -->  acceder grupo filas y columnas por LABEL (ARR TRUE OR FALSE)
segundo = df.loc[1035] # Filtrar por indice (1)
segundo = df.loc[[1035,1036]] # Filtrar por arr indice

segundo = df.loc[3:5] #Filtrado desde x indice hasta y indice
segundo = df.loc[df.index == 1035] #Filtrar por Arreglo -> True, False

segundo = df.loc[1035,'artist']
segundo = df.loc[1035, ['artist','medium']]




# iloc --> Filtrando por los indices

tercero = df.iloc[0]
tercero = df.iloc[[0,1]]
tercero = df.iloc[0:10]
tercero = df.iloc[df.index == 1035]

tercero = df.iloc[0:10, 0:4] # Filtrado indices por rango de indice 0:4




