#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 23:41:03 2019

Genera la Región 4 y la tabla de datos iniciales.

@author: memogarro
"""

import time 
start_time = time.time()

import pandas as pd
import numpy as np
import csv

#MatrizInicial = pd.read_csv('CAux4M-Datos_Iniciales.csv')

DatosIniciales = pd.read_csv('CAux4M-Datos_Iniciales.csv')
Distancia = pd.read_csv('Distancia.csv')

C4M = DatosIniciales['C4M'].values
F4M = DatosIniciales['Ranitas_C4M'].values
Dist = Distancia['Dist'].values

r=192
c=202

I=range(r*c)

R4M=[]
for a in np.arange(r):
    Ba=[]
    for b in np.arange(c):
        Ba.append(r*(c-1-b)+a)
        if C4M[r*(c-1-b)+a]==1:
            break
    R4M.append(Ba)
    
R4M=[y for x in R4M for y in x]

C4M1=[i for i in I if C4M[i]==1]
               
R4M=R4M+C4M1

R4M=list(dict.fromkeys(R4M)) #Quitar repetidos

R4M=sorted(R4M) # Ordenar de menor a mayor

np.save("R4M.npy",R4M)

mR4M=np.zeros((r,c),dtype=int)
for i in np.arange(r):
    for j in np.arange(c):
        k=r*j+i
        if k in R4M:
            mR4M[i][j]=I[k]
            
ID4M=range(len(R4M))

np.save("ID4M.npy",ID4M)

DR4M=[Dist[x] for x in R4M]

np.save("DR4M.npy",DR4M)

FR4M=[F4M[i] for i in R4M]
CR4M=[C4M[i] for i in R4M]

with open('Region4M-Datos_Iniciales.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["R4ID","Identificador","Dist","Ranitas_C4M", "C4M"])
    writer.writerows(zip(ID4M,R4M,DR4M,FR4M,CR4M,))
                    
with open('Matriz_Region4M.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(mR4M)
    
end_time = time.time()
print("Run time = {}".format(end_time - start_time))