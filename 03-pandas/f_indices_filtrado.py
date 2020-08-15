# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 07:34:07 2020

@author: USER
"""

##f_indices_filtrado.py

import pandas as pd

path = "C://GitKraken_Repositorios//py-burbano-erazo-renato-david//03-pandas//data//artwork_data.csv"

df = pd.read_csv(
    path)

serie_artistas_dup = df['artist']

artistas = pd.unique(serie_artistas_dup)

print(type(artistas)) # numpy array

print(artistas.size)
print(len(artistas))

blake = df['artist'] == 'Blake, William'

print(blake.value_counts())

df_blake = df[blake] # DataFrame