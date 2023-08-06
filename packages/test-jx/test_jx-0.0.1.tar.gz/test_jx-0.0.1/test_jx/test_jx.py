#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 21:30:10 2019

@author: lvjingzhe
"""
import numpy as np
import pandas as pd

def meanuncertainty(x,n):
    r=pd.DataFrame([[0]*(len(x)+1-n) for j in range(n)])
    for i in range(len(x)+1-n):
        r[i]=x[i:i+n]
    groupmean=np.mean(r)
    return min(groupmean),max(groupmean)

def varuncertainty(x,n):
    r=pd.DataFrame([[0]*(len(x)+1-n) for j in range(n)])
    for i in range(len(x)+1-n):
        r[i]=x[i:i+n]
    groupmean=np.mean(r)
    groupvar=np.mean((r-groupmean)**2)
    return min(groupvar),max(groupvar)

