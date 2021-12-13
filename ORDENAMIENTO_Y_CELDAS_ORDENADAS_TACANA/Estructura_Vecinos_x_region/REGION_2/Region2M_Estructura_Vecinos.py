#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 11:02:10 2019

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

R2M=np.load("R2M.npy")

ID2M=np.load("ID2M.npy")

V=[] 
for i in I:
    Vi=[]
    if i in R2M:
        if (i-1>=0) and (q[i-1]==q[i]) and (i-1 in R2M):
            Vi.append(i-1)
        if (i+1<=d) and (q[i+1]==q[i]) and (i+1 in R2M):
            Vi.append(i+1)
        if (i-r>=0) and (s[i-r]==s[i]) and (i-r in R2M):
            Vi.append(i-r)
        if (i+r<=d) and (s[i+r]==s[i]) and (i+r in R2M):
            Vi.append(i+r)
        else:
            pass
    else:
        pass
    V.append(Vi)
    
VR2M=[V[i] for i in R2M]
numVR2M=[len(V[i]) for i in R2M]

nVR2M=[[j for j in ID2M if R2M[j] in VR2M[i]] for i in ID2M]

with open('Region2M_Estructura_Vecinos.csv', 'w', newline='',encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(VR2M)
    
with open('Region2M_Estructura_Vecinos_n.csv', 'w', newline='',encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile,delimiter='\t')
    writer.writerows(zip(numVR2M,VR2M))
    
with open('nRegion2M_Estructura_Vecinos.csv', 'w', newline='',encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(nVR2M)

end_time = time.time()
print()
print("Run time = {}".format(end_time - start_time))