import cv2
import numpy as np

from homomorphic import homomorphic

#brightness value
a= 90
b= 98
c= 106
d= 115

#foggy value
e = 38
f = 44
g = 50
h = 55

#gamma value
vs=0.1,2.5
s=0.5,2
m=1,1
l=0.3,1
vl=0.5,1.5

def low_func_avg(value):

    if (value < a):
        p=1
    elif ((value>=a)&(value<b)):
        p=-0.125*(value-a)+1
    else:
        p=0
    return p

def mid_func_avg(value):

    if((value>=a)&(value<b)):
        p=0.125*(value-a)
    elif((value>=b)&(value<c)):
        p=1
    elif((value>=c)&(value<d)):
        p=-0.125*(value-c)+1
    else:
        p=0
    return p

def high_func_avg(value):

    if ((value>=c)&(value < d)):
        p=0.125*(value-c)
    elif (value>=d):
        p=1
    else:
        p=0
    return p

def fuzzy_avg(value):

    l=low_func_avg(value)
    m=mid_func_avg(value)
    h=high_func_avg(value)
    valuelist=[l,m,h]
    p = max(valuelist)
    state = valuelist.index(p)

    if (state == 0):
        if (p == 1):
            result = 'VS'
        else:
            result = 'S'
    elif (state == 1):
        result = 'M'
    elif (state == 2):
        if (p == 1):
            result = 'VL'
        else:
            result = 'L'

    return result

def low_func_std(value):

    if (value < e):
        p=1
    elif ((value>=a)&(value<b)):
        p=-0.167*(value-a)+1
    else:
        p=0
    return p

def mid_func_std(value):

    if((value>=a)&(value<b)):
        p=0.167*(value-a)
    elif((value>=b)&(value<c)):
        p=1
    elif((value>=c)&(value<d)):
        p=-0.167*(value-c)+1
    else:
        p=0
    return p

def high_func_std(value):

    if ((value>=c)&(value < d)):
        p=0.167*(value-c)
    elif (value>=d):
        p=1
    else:
        p=0
    return p

def fuzzy_std(value):

    l=low_func_std(value)
    m=mid_func_std(value)
    h=high_func_std(value)
    valuelist=[l,m,h]
    p = max(valuelist)
    state = valuelist.index(p)

    if (state == 0):
        if (p == 1):
            result = 'VS'
        else:
            result = 'S'
    elif (state == 1):
        result = 'M'
    elif (state == 2):
        if (p == 1):
            result = 'VL'
        else:
            result = 'L'

    return result

def filtersigma(s1,s2):
    if (s1 == 'VS'):
        if(s2 == 'VS'):
            k=vl
        elif(s2=='S'):
            k=vl
        elif(s2=='M'):
            k=l
        elif(s2=='L'):
            k=m
        elif(s2=='VL'):
            k=m
    if (s1 == 'S'):
        if(s2 == 'VS'):
            k=l
        elif(s2=='S'):
            k=l
        elif(s2=='M'):
            k=m
        elif(s2=='L'):
            k=m
        elif(s2=='VL'):
            k=s
    if (s1 == 'M'):
        if(s2 == 'VS'):
            k=m
        elif(s2=='S'):
            k=m
        elif(s2=='M'):
            k=s
        elif(s2=='L'):
            k=s
        elif(s2=='VL'):
            k=vs
    if (s1 == 'L'):
        if(s2 == 'VS'):
            k=l
        elif(s2=='S'):
            k=l
        elif(s2=='M'):
            k=m
        elif(s2=='L'):
            k=m
        elif(s2=='VL'):
            k=s
    if (s1 == 'VL'):
        if(s2 == 'VS'):
            k=vl
        elif(s2=='S'):
            k=l
        elif(s2=='M'):
            k=l
        elif(s2=='L'):
            k=m
        elif(s2=='VL'):
            k=m
    return k

    img = np.float64(img) + 1.0
    img_retinex = singleScaleRetinex(img, variance)
    for i in range(img_retinex.shape[2]):
        unique, count = np.unique(np.int32(img_retinex[:, :, i] * 100), return_counts=True)
        for u, c in zip(unique, count):
            if u == 0:
                zero_count = c
                break
        low_val = unique[0] / 100.0
        high_val = unique[-1] / 100.0
        for u, c in zip(unique, count):
            if u < 0 and c < zero_count * 0.1:
                low_val = u / 100.0
            if u > 0 and c < zero_count * 0.1:
                high_val = u / 100.0
                break            
        img_retinex[:, :, i] = np.maximum(np.minimum(img_retinex[:, :, i], high_val), low_val)
        
        img_retinex[:, :, i] = (img_retinex[:, :, i] - np.min(img_retinex[:, :, i])) / \
                               (np.max(img_retinex[:, :, i]) - np.min(img_retinex[:, :, i])) \
                               * 255
    img_retinex = np.uint8(img_retinex)        
    return img_retinex
