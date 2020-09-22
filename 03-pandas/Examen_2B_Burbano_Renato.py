# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 07:15:02 2020

@author: USER
"""

import pandas as pd
import math
import numpy as np
from numpy import random

#1) Crea un Dataframe de 10 registros y 6 columnas y consigue las 5 primeros y los 5 ultimos registros

matriz = random.randint(15,size=(10,6))

primeros_cinco = matriz[:5]
ultimos_cinco = matriz[5:]

#2) Crear un dataframe pasando un arreglo de numpy de 6 x 4 con una fecha como indice y con columnas A, B, C, D randomico
                
matriz_random = random.rand(6,4)   

segu_df = pd.DataFrame(
    matriz_random,
    columns =[
        'A',
        'B',
        'C',
        'D'
        ],
    index = {
        '2013-01-01',
        '2013-01-02',
        '2013-01-03',
        '2013-01-04',
        '2013-01-05',
        '2013-01-06'
        })

'''
                A         B         C         D
2013-01-01  0.469112 -0.282863 -1.509059 -1.135632
2013-01-02  1.212112 -0.173215  0.119209 -1.044236
2013-01-03 -0.861849 -2.104569 -0.494929  1.071804
2013-01-04  0.721555 -0.706771 -1.039575  0.271860
2013-01-05 -0.424972  0.567020  0.276232 -1.087401
2013-01-06 -0.673690  0.113648 -1.478427  0.524988
'''

#4) Crear un Dataframe con 10 registros y 6 columnas y con una propiedad del Dataframe mostrar las columnas, con otro comando mostrar los valores.


cuarto = np.random.randint(10, size=(10,6))
cuarto_df = pd.DataFrame(cuarto)
print(cuarto_df.columns.tolist())
print(cuarto_df.index.tolist())

#5) Crear un Dataframe con 10 registros y 6 columnas y con una funcion del Dataframe describir estadisticamente el Dataframe

quinto = np.random.randint(-4,4,size=(10,6))
quinto_df = pd.DataFrame(quinto)
print(quinto_df.describe())

#6) Crear un Dataframe con 10 registros y 6 columnas y con una funcion del Dataframe transponer los datos

sexto = np.random.randint(-2,2,size=(10,6))
sexto_df = pd.DataFrame(
    sexto,
    columns =[
        'A',
        'B',
        'C',
        'D',
        'E',
        'F'
        ],
    index = {
        'num1',
        'num2',
        'num3',
        'num4',
        'num5',
        'num6',
        'num7',
        'num8',
        'num9',
        'num0',
        })
sexto_trans = sexto_df.T

#7) Crear un Dataframe con 10 registros y 6 columnas y Ordenar el dataframe 1 vez por cada columna, ascendente y descendente

sept_df = sexto_df
by_A = sept_df.sort_values('A')
by_A_des = sept_df.sort_values('A', ascending=False)
by_B = sept_df.sort_values('B')
by_B_des = sept_df.sort_values('B', ascending=False)
by_C = sept_df.sort_values('C')
by_C_des = sept_df.sort_values('C', ascending=False)
by_D = sept_df.sort_values('D')
by_D_des = sept_df.sort_values('D', ascending=False)
by_E = sept_df.sort_values('E')
by_E_des = sept_df.sort_values('E', ascending=False)
by_F = sept_df.sort_values('F')
by_F_des = sept_df.sort_values('F', ascending=False)



#8) Crear un Dataframe con 10 registros y 6 columnas llenas de números randomicos del 1 al 10 y seleccionar en un nuevo Dataframe solo los valores mayores a 7

oct = np.random.randint(1,10,size=(10,6))
oct_df = pd.DataFrame(oct)

mayores_siete = oct_df > 7
print(oct_df[mayores_siete])


#9) Crear un Dataframe con 10 registros y 6 columnas llenas de números randomicos del 1 al 10 o valores NaN. Luego llenar los valores NaN con 0.

noven_NaN = oct_df[mayores_siete]
noven_Lleno = noven_NaN.fillna(0)


#10) Crear un Dataframe con 10 registros y 6 columnas llenas de números randomicos del 1 al 10 y sacar la media, la mediana, el promedio

decim = np.random.randint(30,size=(10,6))
decim_df = pd.DataFrame(decim)
print(decim_df.mean())
print(decim_df.median())
print(decim_df.mode())


#11) Crear un Dataframe con 10 registros y 6 columnas llenas de números randomicos del 1 al 10, luego crear otro dateframe con 10 registros y 6 columnas llenas de números randomicos del 1 al 10 y anadirlo al primer Dataframe

oncea = np.random.randint(1,10,size=(10,6))
oncea_df = pd.DataFrame(oncea)
oncea_dos = np.random.randint(1,10,size=(10,6))
oncea_dos_df = pd.DataFrame(oncea_dos)

oncea_df =  vertical_stack = pd.concat([oncea_df, oncea_dos_df])


#12) Crear un Dataframe con 10 registros y 6 columnas llenas de strings. Luego, unir la columna 1 y 2 en una sola, la 3 y 4, y la 5 y 6 concatenando su texto.

path = "C://GitKraken_Repositorios//py-burbano-erazo-renato-david//03-pandas//data//artwork_data.csv"

columnas = ['artist','title','medium','creditLine','dimensions','units']

doce_df = pd.read_csv(
    path,
    usecols = columnas,
    nrows=10)

doce_df["1 + 2"] = doce_df["artist"] + " " + doce_df["title"]
doce_df["3 + 4"] = doce_df["medium"] + " " + doce_df['creditLine']
doce_df["5 + 6"] = doce_df['dimensions'] + " " + doce_df['units']


#13) Crear un Dataframe con 10 registros y 6 columnas llenas de números randomicos del 1 al 10 enteros, obtener la frecuencia de repeticion de los numeros enteros en cada columna


trec = np.random.randint(1,10,size=(10,6))
trec_df = pd.DataFrame(trec)
print(trec_df[0].value_counts())
print(trec_df[1].value_counts())
print(trec_df[2].value_counts())
print(trec_df[3].value_counts())
print(trec_df[4].value_counts())
print(trec_df[5].value_counts())

#14) Crear un Dataframe con 10 registros y 3 columnas, A B C, llenas de números randomicos del 1 al 10 enteros. Crear una nueva columna con el calculo por fila (A * B ) / C

