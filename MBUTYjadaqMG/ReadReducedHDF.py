#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 14:54:33 2024

@author: francescopiscitelli
"""

import numpy as np
import h5py
import os 
import sys 
from lib import libLoadFile as loa 


###############################################################################


datapathinput         = os.path.abspath('.')+'/data/' 

filename = 'fullTest-240912-100058-reduced-PY-From000To000.h5'

DurationsALL, MONdata, MONcounts, He3data, He3counts, MOVMMdata, data = loa.readHDFreducedFileMG(datapathinput+filename)



# if os.path.exists(datapathinput+filename) is False:
#      print('\n \033[1;33mWARNING: Reduced DATA file does not exist.\033[1;37m')
#      sys.exit()


# f = h5py.File(datapathinput+filename, "r")

# for key in f.keys():
#        # print(key)
#        name = key
     
# ff = f[name]

# # for key in ff.keys():
# #       print(key)

# ########################################

# try:
#     rtemp = ff['run']
#     TotalDuration    = rtemp['TotalDuration'][()]
#     Durations        = rtemp['Durations'][()]
#     duration         = rtemp['duration'][()]
#     TotalDurationOD  = rtemp['TotalDurationOtherDigit'][()]
#     DurationsOD      = rtemp['DurationsOtherDigit'][()]
#     durationOD       = rtemp['durationOtherDigit'][()]
# except:
#     print('--> no run info')
#     TotalDuration    = 0
#     Durations        = 0
#     duration         = 0
#     TotalDurationOD  = 0
#     DurationsOD      = 0
#     durationOD       = 0
    
    
# DurationsALL = {
    
#     "TotalDuration" : TotalDuration,
#     "Durations" : Durations,
#     "duration" : duration,
#     "TotalDurationOD" : TotalDurationOD,
#     "DurationsOD" : DurationsOD,
#     "durationOD" : durationOD

    
#     }    
     
# ########################################

# # try:
# #     rtemp = ff['instrument']
# #     TotalDuration    = rtemp['TotalDuration'][()]
# #     Durations        = rtemp['Durations'][()]
# #     duration         = rtemp['duration'][()]
# #     TotalDurationOD  = rtemp['TotalDurationOtherDigit'][()]
# #     DurationsOD      = rtemp['DurationsOtherDigit'][()]
# #     durationOD       = rtemp['durationOtherDigit'][()]
# # except:
# #     print('--> no run info')
# #     TotalDuration    = 0
# #     Durations        = 0
# #     duration         = 0
# #     TotalDurationOD  = 0
# #     DurationsOD      = 0
# #     durationOD       = 0
         
# ######################################## 
   
# try:
#     mtemp   = ff['monitor']
#     MONdata = mtemp['data'][()]  #
#     MONcounts = mtemp['counts'][()]  #
#     if np.shape(MONdata)[0] == 0 :
#         print('\033[1;33m--> no monitor data\033[1;37m')
        
# except:
#     print('\033[1;33m--> no monitor data\033[1;37m')
#     MONdata = -1*np.ones((1,4),dtype=float)
#     MONcounts = 0
    
# ########################################    

# try:
#     mtemp   = ff['He3tube']
#     He3data = mtemp['data'][()]  #
#     He3counts = mtemp['counts'][()]  #
    
#     if np.shape(He3data)[0] == 0 :
#         print('\033[1;33m--> no He3 tube data\033[1;37m')
        
# except:
#     print('\033[1;33m--> no He3 tube data\033[1;37m')
#     He3data   = -1*np.ones((1,4),dtype=float)
#     He3counts = 0
        
# ########################################

# try:
#     mtemp   = ff['MOVMM']
#     MOVMMdata = mtemp['data'][()]  
    
#     if np.shape(MOVMMdata)[0] == 0 :
#         print('\033[1;33m--> no MO VMM data\033[1;37m')

# except:
#     print('\033[1;33m--> no MO VMM data\033[1;37m')
#     MOVMMdata = -1*np.ones((1,4),dtype=float)


# ########################################

# try:
#     dtemp = ff['detector']
#     arrangement = np.int64(dtemp['arrangement'][()])
    
#     items = list(dtemp.keys())
    
#     stringToFind = 'digit'
    
#     presentDigit = []
    
#     data = []
    
#         # for k, dset in enumerate(dtemp.keys()) :
        
#     #     print (k, dset)
    
#     for k in range(len(items)):    
#         if stringToFind in items[k]:
#             # print(items[k],k)
#             temp =  items[k].split(stringToFind)
#             presentDigit = np.append(presentDigit,np.int64(temp[1]))
    
#     for digit in presentDigit :
        
#         selDigit = stringToFind+str(int(digit))
#         dataTemp = dtemp[selDigit]['data'][()]
        
#         data.append(dataTemp)
        
        
#     # if not(digitID in presentDigit):
#     #     data = np.ones((1,9),dtype=float)*np.inf                
#     #     print('\n \t \033[1;31mWARNING: No Digit ',str(digitID),' found! This file only contains Digitizers:', end=' ')
#     #     for digit in presentDigit:
#     #         print(np.int(digit),end=' ')
#     #     print('\033[1;37m')
        
#     # else:

#     #     selDigit = stringToFind+str(digitID)
    
#     #     for k in range(len(items)):    
#     #         if selDigit in items[k]:
#     #             # print(items[k])
#     #             data = dtemp[selDigit]['data'][()]
               
# except:
#     print('\033[1;33m--> no detector data\033[1;37m')
#     # arrangement = 0
#     data        = -1*np.ones((1,9),dtype=float)
    
# f.close() 