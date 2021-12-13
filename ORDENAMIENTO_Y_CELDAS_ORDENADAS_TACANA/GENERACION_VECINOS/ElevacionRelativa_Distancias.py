#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 12:17:11 2019

@author: memogarro

Genera la elevación relativa al rio de cada centroide de las celdas de la Lattice
"""

import time
start_time = time.time()

import pandas as pd
import numpy as np
#import builtins
import csv

GeneracionVecinos = pd.read_csv('Generacion_Vecinos.csv')
ElevacionCentroides = pd.read_csv('Centroides-Elevacion_QGIS.csv')
G = GeneracionVecinos['Generacion'].values
E = ElevacionCentroides['Z'].values

with open("Estructura_Vecinos.csv", newline='') as csvfile:
    reader = csv.reader(csvfile)
    V=[]
    for row in reader:
        V.append(list(map(int,row)))

r=192
c=202

I=range(r*c)

mG=[min([G[j] for j in V[i]]) for i in I]

def mV(i):
    for j in V[i]:
        if G[j]==mG[i]:
            mVi=j
    return mVi

p=[]
for i in I:
    pi=[]
    if G[i]==0:
        pi.append(i)
    else:
        j=mV(i)
        pi.append(j)
        t=G[j]
        while t>0:
            j=mV(j)
            pi.append(j)
            t=G[j]
    p.append(pi)

aux=[[j for j in p[i] if G[j]==0] for i in I]

aux=[E[y] for x in aux for y in x]

elev=[abs(E[i]-aux[i])//5 for i in I]

np.save("elev.npy",elev)

dist=[int(G[i]+elev[i]) for i in I]

np.save("dist.npy",dist)

with open('Elevacion_Relativa.csv', 'w', newline='',encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["I","Elev_Rel"])
    writer.writerows(zip(I,elev))

with open('Distancia.csv', 'w', newline='',encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["I","Dist"])
    writer.writerows(zip(I,dist))

end_time = time.time()
print()
print("Run time = {}".format(end_time - start_time))
