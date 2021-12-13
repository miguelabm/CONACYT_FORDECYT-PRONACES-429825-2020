#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 12:30:18 2019

Genera la Región 3 y la tabla de datos iniciales.

@author: memogarro
"""

import time 
start_time = time.time()

import pandas as pd
import numpy as np
import csv

DatosIniciales = pd.read_csv('CAux5M-Datos_Iniciales.csv')
Distancia = pd.read_csv('Distancia.csv')

C5M = DatosIniciales['C5M'].values
F5M = DatosIniciales['Ranitas_C5M'].values
Dist = Distancia['Dist'].values

r=192
c=202

r0=138

R=range(r)
C=range(c)
I=range(r*c)

R3Aux=[i for i in I if i%r<=r0]

C5M1=[i for i in I if C5M[i]==1]
    
R3M=[]
for x in range(r0+1):
    minimox=min(i for i in C5M1 if i%r==x)
    maximox=max(i for i in C5M1 if i%r==x)
    R3Mx=[i for i in R3Aux if i%r==x and minimox<=i<=maximox]
    R3M.append(R3Mx)
    
R3M=[y for x in R3M for y in x]

#R3M.sort()
R3M=sorted(R3M)

np.save("R3M.npy",R3M)

ID3M=range(len(R3M))

np.save("ID3M.npy",ID3M)

DR3M=[Dist[x] for x in R3M]

np.save("DR3M.npy",DR3M)

mR3M=np.zeros((r,c),dtype=int)
for i in R:
    for j in C:
        k=r*j+i
        if k in R3M:
            mR3M[i][j]=k

FR3M=[F5M[i] for i in R3M]
CR3M=[C5M[i] for i in R3M]

with open('Region3M-Datos_Iniciales.csv', 'w', newline='', encoding='utf-8') as csvfile: 
    writer = csv.writer(csvfile)
    writer.writerow(["R3ID","Identificador", "Dist","Ranitas_C5M","C5M"])
    writer.writerows(zip(ID3M,R3M,DR3M,FR3M,CR3M,))
                    
with open('Matriz_Region3M.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(mR3M)
      
end_time = time.time()
print()
print("Run time = {}".format(end_time - start_time))