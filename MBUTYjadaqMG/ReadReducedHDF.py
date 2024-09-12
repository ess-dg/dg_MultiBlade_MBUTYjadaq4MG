#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 14:54:33 2024

@author: francescopiscitelli
"""

import numpy as np
import h5py
import os 


###############################################################################


datapathinput         = os.path.abspath('.')+'/data/' 

filename = 'fullTest-240912-100058-reduced-PY-From000To000.h5'


f = h5py.File(datapathinput+filename, "r")

for key in f.keys():
       # print(key)
       name = key
     
ff = f[name]

# for key in ff.keys():
#       print(key)

try:
    rtemp = ff['run']
    duration = rtemp['TotalDuration'][()]
    durationAll = rtemp['Durations'][()]
except:
    print('--> no run info')
    duration = 0
    durationAll = 0
 
try:
    mtemp   = ff['monitor']
    MONdata = mtemp['data'][()]  #
    MONcounts = mtemp['counts'][()]  #
except:
    print('--> no monitor')
    MONdata = np.ones((1,2),dtype=float)*np.inf
    MONcounts = 0

try:
    dtemp = ff['detector']
    arrangement = np.float64(dtemp['arrangement'][()])
    
    items = list(dtemp.keys())
    
    stringToFind = 'digit'
    
    presentDigit = []
    
        # for k, dset in enumerate(dtemp.keys()) :
        
    #     print (k, dset)
    
    for k in range(len(items)):    
        if stringToFind in items[k]:
            # print(items[k],k)
            temp =  items[k].split(stringToFind)
            presentDigit = np.append(presentDigit,np.int64(temp[1]))
    
    if not(digitID in presentDigit):
        data = np.ones((1,9),dtype=float)*np.inf                
        print('\n \t \033[1;31mWARNING: No Digit ',str(digitID),' found! This file only contains Digitizers:', end=' ')
        for digit in presentDigit:
            print(np.int(digit),end=' ')
        print('\033[1;37m')
        
    else:

        selDigit = stringToFind+str(digitID)
    
        for k in range(len(items)):    
            if selDigit in items[k]:
                # print(items[k])
                data = dtemp[selDigit]['data'][()]
               
except:
    print('\033[1;33m-->WARNING: no detector data\033[1;37m')
    # arrangement = 0
    data        = np.ones((1,9),dtype=float)*np.inf
    
f.close() 