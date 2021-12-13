#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 11:54:30 2019

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

R1M=np.load("R1M.npy")

ID1M=np.load("ID1M.npy")

V=[] 
for i in I:
    Vi=[]
    if i in R1M:
        if (i-1>=0) and (q[i-1]==q[i]) and (i-1 in R1M):
            Vi.append(i-1)
        if (i+1<=d) and (q[i+1]==q[i]) and (i+1 in R1M):
            Vi.append(i+1)
        if (i-r>=0) and (s[i-r]==s[i]) and (i-r in R1M):
            Vi.append(i-r)
        if (i+r<=d) and (s[i+r]==s[i]) and (i+r in R1M):
            Vi.append(i+r)
        else:
            pass
    else:
        pass
    V.append(Vi)
    
VR1M=[V[i] for i in R1M]
numVR1M=[len(V[i]) for i in R1M]

nVR1M=[[j for j in ID1M if R1M[j] in VR1M[i]] for i in ID1M]

with open('Region1M_Estructura_Vecinos.csv', 'w', newline='',encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(VR1M)
    
with open('Region1M_Estructura_Vecinos_n.csv', 'w', newline='',encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile,delimiter='\t')
    writer.writerows(zip(numVR1M,VR1M))
    
with open('nRegion1M_Estructura_Vecinos.csv', 'w', newline='',encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(nVR1M)

end_time = time.time()
print()
print("Run time = {}".format(end_time - start_time))