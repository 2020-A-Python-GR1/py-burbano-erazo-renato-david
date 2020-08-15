# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 09:14:39 2020

@author: USER
"""

import numpy as np
import pandas as pd
from scipy import ndimage
from scipy import misc
import matplotlib.pyplot as plt

## 2) Crear un vector de ceros de tamaÃ±o 10

vector_ceros = np.zeros(10)


## 3) Crear un vector de ceros de tamaÃ±o 10 y el de la posicion 5 sea igual a 1

vector_ceros[5] = 1

## 4) Cambiar el orden de un vector de 50 elementos, el de la posicion 1 es el de la 50 etc.

vector_cincuenta = np.arange(50)
vector_cincuenta = vector_cincuenta[::-1]

## 5) Crear una matriz de 3 x 3 con valores del cero al 8

matriz_tres = np.arange(9).reshape(3,3)

## 6) Encontrar los indices que no sean cero en un arreglo

arreglo = [1,2,0,0,4,0]

encontrar = np.array(arreglo) !=0


## 7) Crear una matriz de identidad 3 x 3 

identidad = np.eye(3)

## 8) Crear una matriz 3 x 3 x 3 con valores randomicos

matriz_random = np.random.randint(0,27,27).reshape(3,3,3)


## 9) Crear una matriz 10 x 10 y encontrar el mayor y el menor

matriz_diez = np.random.randint(0,15,100).reshape(10,10)
print(matriz_diez.max())
print(matriz_diez.min())


## 10) Sacar los colores RGB unicos en una imagen (cuales rgb existen ej: 0, 0, 0 - 255,255,255 -> 2 colores)

mapache = misc.face()
unicos = np.unique(mapache.reshape(-1, mapache.shape[2]), axis=0)

## 11) Â¿Como crear una serie de una lista, diccionario o arreglo?

mylist = list('abcedfghijklmnopqrstuvwxyz')
myarr = np.arange(26)
mydict = dict(zip(mylist, myarr))

serie_lista = pd.Series(mylist)
serie_arreglo = pd.Series(myarr)
serie_diccionario = pd.Series(mydict)


## 12) Â¿Como convertir el indice de una serie en una columna de un DataFrame?


mylist = list('abcedfghijklmnopqrstuvwxyz')
myarr = np.arange(26)
mydict = dict(zip(mylist, myarr))
ser = pd.Series(mydict) 
# Transformar la serie en dataframe y hacer una columna indice
ser = pd.DataFrame(ser,index_col = 0)


## 13) Â¿Como combinar varias series para hacer un DataFrame?

ser1 = pd.Series(list('abcedfghijklmnopqrstuvwxyz'))
ser2 = pd.Series(np.arange(26))

combinar_series = pd.DataFrame(ser1,ser2)


## 14) Â¿Como obtener los items que esten en una serie A y no en una serie B?

ser1 = pd.Series([1, 2, 3, 4, 5])
ser2 = pd.Series([4, 5, 6, 7, 8])


def comparar(valor_serie):
    comp = False
    for val in ser2:
        if(valor_serie != val):
            comp = True
        else:
            return None
    if(comp):
        return valor_serie
    
obtener_items = ser1.map(comparar)
 


## 15) Â¿Como obtener los items que no son comunes en una serie A y serie B?


ser1 = pd.Series([1, 2, 3, 4, 5])
ser2 = pd.Series([4, 5, 6, 7, 8])

def noComunes(valor_serie):
    comp = False
    for val in ser2:
        if(valor_serie != val):
            comp = True
        else:
            return None
    if(comp):
        return valor_serie
    
no_comues = ser1.map(noComunes)


## 16) Â¿Como obtener el numero de veces que se repite un valor en una serie?

ser = pd.Series(np.take(list('abcdefgh'), np.random.randint(8, size=30)))

ser = pd.DataFrame(ser)
numero_veces = ser[0].value_counts()


## 17) Â¿Como mantener los 2 valores mas repetidos de una serie, y a los demas valores cambiarles por 0 ?


np.random.RandomState(100)
ser = pd.Series(np.random.randint(1, 5, [12]))

ser_dataframe = pd.DataFrame(ser)
repeticiones = ser_dataframe[0].value_counts()
mantener_valores = repeticiones.head(2)

def ponerCeros(valor_serie):
    for val in mantener_valores.index:
        if(valor_serie != val):
            return 0
        else:
            return valor_serie
    
nuevo_ser = ser.map(ponerCeros)


## 18) Â¿Como transformar una serie de un arreglo de numpy a un DataFrame con un `shape` definido?


ser = pd.Series(np.random.randint(1, 10, 35))


tranformar = pd.DataFrame(ser,columns=7,index=5)

## 19) Â¿Obtener los valores de una serie conociendo la posicion por indice?

'''
```python
ser = pd.Series(list('abcdefghijklmnopqrstuvwxyz'))
pos = [0, 4, 8, 14, 20]
# a e i o u
```

## 20) Â¿Como anadir series vertical u horizontalmente a un DataFrame?


```python
ser1 = pd.Series(range(5))
ser2 = pd.Series(list('abcde'))
```


## 21)Â¿Obtener la media de una serie agrupada por otra serie?

`groupby` tambien esta disponible en series.


```python
frutas = pd.Series(np.random.choice(['manzana', 'banana', 'zanahoria'], 10))
pesos = pd.Series(np.linspace(1, 10, 10))
print(pesos.tolist())
print(frutas.tolist())
#> [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]
#> ['banana', 'carrot', 'apple', 'carrot', 'carrot', 'apple', 'banana', 'carrot', 'apple', 'carrot']

# Los valores van a cambiar por ser random
# apple     6.0
# banana    4.0
# carrot    5.8
# dtype: float64

```
'''

## 22)Â¿Como importar solo columnas especificas de un archivo csv?

##https://raw.githubusercontent.com/selva86/datasets/master/BostonHousing.csv.

path = "C://GitKraken_Repositorios//py-burbano-erazo-renato-david//03-pandas//data//BostonHousing.csv"

df1 = pd.read_csv(
    path,
    nrows=10)

columnas = ['crim','zn','indus','chas','nox','rm','age']

df2 = pd.read_csv(path, nrows = 10, usecols = columnas)

df3 = pd.read_csv(path, nrows = 10, usecols = columnas, index_col = 'crim')


