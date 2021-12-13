#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 11:43:17 2019

@author: memogarro
"""

import time 
start_time = time.time()

import pandas as pd
import numpy as np
import csv

DatosIniciales = pd.read_csv('C1M-Datos_Iniciales.csv')
Distancia = pd.read_csv('Distancia.csv')

C1M = DatosIniciales['C1M'].values
F1M = DatosIniciales['Ranitas_C1M'].values
Dist = Distancia['Dist'].values

r=192
c=202

I=list(range(r*c))

C1M1=[i for i in I if C1M[i]==1]
    
R1M=[]
for x in range(r):
    maximox=max(i for i in C1M1 if i%r==x)
    R1Mx=[i for i in I if i%r==x and i<=maximox]
    R1M.append(R1Mx)
    
R1M=[y for x in R1M for y in x]

#R3M.sort()
R1M=sorted(R1M)

np.save("R1M.npy",R1M)

ID1M=range(len(R1M))

np.save("ID1M.npy",ID1M)

DR1M=[Dist[x] for x in R1M]

np.save("DR1M.npy",DR1M)

mR1M=np.zeros((r,c),dtype=int)
for i in range(r):
    for j in range(c):
        k=r*j+i
        if k in R1M:
            mR1M[i][j]=k

FR1M=[F1M[i] for i in R1M]
CR1M=[C1M[i] for i in R1M]

with open('Region1M-Datos_Iniciales.csv', 'w', newline='', encoding='utf-8') as csvfile: 
    writer = csv.writer(csvfile)
    writer.writerow(["R1ID","Identificador", "Dist","Ranitas_C1M","C1M"])
    writer.writerows(zip(ID1M,R1M,DR1M,FR1M,CR1M,))
                    
with open('Matriz_Region1M.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(mR1M)
      
end_time = time.time()
print()
print("Run time = {}".format(end_time - start_time))