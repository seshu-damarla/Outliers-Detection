# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 14:35:48 2022

@author: Seshu Kumar Damarla
"""

"""
Detection of outliers using meadian absolute deviation
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math

data = pd.read_csv('data.csv',header=None)
data=np.array(data)

plt.plot(data,'-o')
plt.show()

def median_absolute_deviation(data):
    n=data.shape[0]

    ar=(n+1)/2 # average rank

    M1=0
    M2=0
    M=0
    if (ar%2)==0:
        print(math.trunc(ar))
#    print(1)
        M=data[math.trunc(ar)]
    else:
        ar1=math.trunc(ar)
        M1=data[ar1-1]
        M2=data[ar1]
        M=(M1+M2)/2
    
    # |x-M|
    # absolute deviation from median
    data1=abs(data-M)
    data2=np.sort(np.array(data1),axis=0)
    # median absolute deviation
    m1=0
    m2=0
    m=0
    b=1.4826

    if (ar%2)==0:
        m=data1[math.trunc(ar)]
        MAD=b*m
    else:
        ar1=math.trunc(ar)
        m1=data2[ar1-1]
        m2=data2[ar1]
        m=(m1+m2)/2
        MAD=b*m

    lowerlimit=M-3*MAD
    upperlimit=M+3*MAD

    LL=data<lowerlimit
    UL=data>=upperlimit

    idx_outliers=[]
    for i in range(LL.shape[0]):
        if LL[i]==True:
            idx_outliers.append(i)
        
        if UL[i]==True:
            idx_outliers.append(i)
        
    data_nooutliers=np.delete(data,idx_outliers)
    outliers=data[idx_outliers]
    return data_nooutliers, outliers


X, Y=median_absolute_deviation(data)

print(Y)
plt.plot(X)
plt.show()

