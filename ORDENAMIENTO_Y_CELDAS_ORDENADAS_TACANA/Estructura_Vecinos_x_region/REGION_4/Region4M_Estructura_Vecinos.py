#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 15:57:49 2019

@author: memogarro
"""

import time 
start_time = time.time()

#import pandas as pd
import numpy as np
import csv

#with open("Estructura_Vecinos.csv", newline='') as csvfile:
#    reader = csv.reader(csvfile)
#    V=[]
#    for row in reader:
#        V.append(list(map(int,row)))

r=192 
c=202 

d=r*c-1

I=range(r*c)

s=[i%r for i in I]

q=[np.floor(i/r) for i in I]
q=[y.astype(int) for y in q]

Region4M=np.load("Region4M.npy")

ID4M=np.load("ID4M.npy")

V=[] # Vector cuya entrada i es igual al vector de sitios vecinos del sitio i
for i in I:
    Vi=[] # Vector cuyas entradas son los sitios vecinos del sitio i
    if i in Region4M:
        if (i-1>=0) and (q[i-1]==q[i]) and (i-1 in Region4M):
            Vi.append(i-1)
        if (i+1<=d) and (q[i+1]==q[i]) and (i+1 in Region4M):
            Vi.append(i+1)
        if (i-r>=0) and (s[i-r]==s[i]) and (i-r in Region4M):
            Vi.append(i-r)
        if (i+r<=d) and (s[i+r]==s[i]) and (i+r in Region4M):
            Vi.append(i+r)
        else:
            pass
    else:
        pass
    V.append(Vi)
    
VR4M=[V[i] for i in Region4M]

nVR4M=[[j for j in ID4M if Region4M[j] in VR4M[i]] for i in ID4M]

with open('Region4M_Estructura_Vecinos.csv', 'w', newline='',encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(VR4M)
    
with open('nRegion4M_Estructura_Vecinos.csv', 'w', newline='',encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(nVR4M)

end_time = time.time()
print()
print("Run time = {}".format(end_time - start_time))