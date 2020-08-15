# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 21:49:20 2020

@author: USER
"""


import pandas as pd
import numpy as np
import os
import xlsxwriter

path = "C://GitKraken_Repositorios//py-burbano-erazo-renato-david//03-pandas//data//artwork_data.csv"

df = pd.read_csv(
    path)

sub_df = df.iloc[49980:50519,:].copy()

path_excel = "C://GitKraken_Repositorios//py-burbano-erazo-renato-david//Deberes//Deber_3//Deber_Grafico_excel.xlsx"

num_artistas = sub_df['artist'].value_counts()

workbook = xlsxwriter.Workbook(path_excel)

worksheet = workbook.add_worksheet()
chart = workbook.add_chart({'type': 'pie'})

worksheet.write_column('A2',num_artistas.index)
worksheet.write_column('B2',num_artistas.values)

chart.set_title({
    'name': 'PIE Artitas',
    'name_font': {
        'name': 'Calibri',
        'color': 'blue',
    },
})

chart.add_series({

    'categories': '=Sheet1!$A$2:$A$85',
    'values':     '=Sheet1!$B$2:$B$85',
})

worksheet.insert_chart('C3', chart)

workbook.close()



