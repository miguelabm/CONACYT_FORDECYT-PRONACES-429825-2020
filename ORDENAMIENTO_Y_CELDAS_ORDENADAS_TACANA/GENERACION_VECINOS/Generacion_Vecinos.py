#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 18:51:59 2019

@author: memogarro

Genera la estructura de vecinos por generación
"""

import time
start_time = time.time()

import pandas as pd
import numpy as np
import csv

MatrizInicial = pd.read_csv('Sitios_Rio.csv')

I = MatrizInicial['Identificador'].values
R = MatrizInicial['Rio'].values

d=len(I)-1

r=192 # Número de renglones de la matriz de sitios
c=202 # Número de columnas de la matriz de sitios (solo se usa para crear la matriz final)

# Renglones de la matriz de sitios
s=I%r

# Columnas de la matriz de sitios
u=np.floor(I*(1/r))
u=u.astype(int)

#z=list(zip(I,s,u)) # Matriz de Indentificador i y coordenadas (s,u) correspondientes

v=[] # Vector cuya entrada i es igual al vector de sitios vecinos del sitio i
for i in I:
    vi=[] # Vector cuyas entradas son los sitios vecinos del sitio i
    if (i-1>=0) and (u[i-1]==u[i]):
        vi.append(i-1)
    if (i+1<=d) and (u[i+1]==u[i]):
        vi.append(i+1)
    if (i-r>=0) and (s[i-r]==s[i]):
        vi.append(i-r)
    if (i+r<=d) and (s[i+r]==s[i]):
        vi.append(i+r)
    v.append(vi)

R0=[i for i in I if R[i]==1] # Conjunto de sitios donde hay río. Generación 0

S0=[i for i in I if R[i]==0] # Conjunto de sitios donde no hay río

R=[1-R[i] for i in I] # Cambiamos 0 en el río y 1 en otro caso

# Loop para crear y etiquetar paso a paso las fronteras a partir del río
k=1*(len(R0)>0)*(len(S0)>0)

while k>0:
    R1=[] # Sitios frontera del conjunto de sitios R0. Generación k
    for i in S0:
        for j in R0:
            if i in v[j]:
                R1.append(i)
    R1 = list(dict.fromkeys(R1)) # Quitamos sitios repetidos de la lista R1

    S1=[] # Nivel de la generación k
    for i in S0:
        if i in R1:
            pass
        else:
            S1.append(i)
    S1 = list(dict.fromkeys(S1)) # Quitamos sitios repetidos de la lista S1

    R0=[i for i in R1] # Redefinición de R0 y R1 para el paso siguiente
    S0=[i for i in S1]

    # Nueva matriz R
    for i in I:
        if i in R0:
            R[i]=k
        elif i in R1:
            R[i]=k+1
        else:
            pass

    k=(k+1)*(len(S0)>0)

# Creamos la matriz R
mR = np.zeros((r,c),dtype=int)
for i in np.arange(r):
    for j in np.arange(c):
        l=r*j+i
        mR[i][j] = R[l]

with open('Generacion_Vecinos.csv', 'w', newline='',encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Identificador", "Generacion"])
    writer.writerows(zip(I,R))

with open('Matriz_Generacion_Vecinos.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(mR)


end_time = time.time()
print()
print("Run time = {}".format(end_time - start_time))
