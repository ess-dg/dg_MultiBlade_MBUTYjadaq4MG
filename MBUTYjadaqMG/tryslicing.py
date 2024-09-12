#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 14:39:00 2024

@author: francescopiscitelli
"""

import numpy as np

aa = np.ones((20,4))

aa[0:3,1] = 8
aa[3:7,1] = 14
aa[7:10,1] = 5
aa[10:,1] = 9



aa[0:3,2] = 88
aa[3:7,2] = 148
aa[7:10,2] = 58
aa[10:,2] = 98


ch = [14,9]


# for ch
# sel = aa[:,1] == ch


for kk, mmo in enumerate(ch):
    
    print(kk)
    print(mmo)

