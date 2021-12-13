#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 14:01:07 2019

@author: memogarro
"""

import time 
start_time = time.time()

import pandas as pd
import numpy as np
import csv

DatosIniciales = pd.read_csv('CAux6M-Datos_Iniciales.csv')
Distancia = pd.read_csv('Distancia.csv')

C6M = DatosIniciales['C6M'].values
F6M = DatosIniciales['Ranitas_C6M'].values
Dist = Distancia['Dist'].values

r=192
c=202

I=list(range(r*c))

C6M1=[i for i in I if C6M[i]==1]
    
R2M=[]
for x in range(r):
    minimox=min(i for i in C6M1 if i%r==x)
    maximox=max(i for i in C6M1 if i%r==x)
    R2Mx=[i for i in I if i%r==x and minimox<=i<=maximox]
    R2M.append(R2Mx)
    
R2M=[y for x in R2M for y in x]

#R3M.sort()
R2M=sorted(R2M)

np.save("R2M.npy",R2M)

ID2M=range(len(R2M))

np.save("ID2M.npy",ID2M)

DR2M=[Dist[x] for x in R2M]

np.save("DR2M.npy",DR2M)

mR2M=np.zeros((r,c),dtype=int)
for i in range(r):
    for j in range(c):
        k=r*j+i
        if k in R2M:
            mR2M[i][j]=k

FR2M=[F6M[i] for i in R2M]
CR2M=[C6M[i] for i in R2M]

with open('Region2M-Datos_Iniciales.csv', 'w', newline='', encoding='utf-8') as csvfile: 
    writer = csv.writer(csvfile)
    writer.writerow(["R2ID","Identificador", "Dist","Ranitas_C6M","C6M"])
    writer.writerows(zip(ID2M,R2M,DR2M,FR2M,CR2M,))
                    
with open('Matriz_Region2M.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(mR2M)
      
end_time = time.time()
print()
print("Run time = {}".format(end_time - start_time))