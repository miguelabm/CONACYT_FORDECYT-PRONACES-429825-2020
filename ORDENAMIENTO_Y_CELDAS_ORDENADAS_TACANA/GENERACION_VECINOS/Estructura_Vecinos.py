#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 13:42:29 2019

@author: memogarro

Genera la estructura de vecinos de la matriz de la lattice de sitios de 192x202
"""

import time
start_time = time.time()

import numpy as np
import csv

r=192
c=202

I=range(r*c)

d=r*c-1

s=[i%r for i in I]

u=[int(np.floor(i/r)) for i in I]

v=[]
for i in I:
    vi=[]
    if (i-1>=0) and (u[i-1]==u[i]):
        vi.append(i-1)
    if (i+1<=d) and (u[i+1]==u[i]):
        vi.append(i+1)
    if (i-r>=0) and (s[i-r]==s[i]):
        vi.append(i-r)
    if (i+r<=d) and (s[i+r]==s[i]):
        vi.append(i+r)
    v.append(vi)

with open('Estructura_Vecinos.csv', 'w', newline='',encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(v)

end_time = time.time()
print()
print("Run time = {}".format(end_time - start_time))
