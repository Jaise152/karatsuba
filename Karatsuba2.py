# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 11:44:05 2019

@author: 611916967
"""

def ceil(n):
    res = int(n)
    return res if res == n or n < 0 else res+1

def floor(n):
    res = int(n)
    return res if res == n or n >= 0 else res-1

def karastuba(x,y):
    if x < 10 and y <10:
        return x*y
    n = max(len(str(x)),len(str(y)))
    m = int(ceil(float(n)/2))
    x_H = int(floor(x/10**m))
    x_L = int(x%(10**m))
#    print (x,y)
#    print(x_H,x_L)
    y_H = int(floor(y/10**m))
    y_L = int(y%(10**m))
#    print(y_H,y_L)
    S1 = karastuba(x_H,y_H)
    S2 = karastuba(x_L,y_L)
    S3 = karastuba(x_H,y_L)
    S4 = karastuba(x_L,y_H)
    S5 = karastuba(x_H + x_L , y_H + y_L)
    S6 = S5 - S1 -S2
    Karatsuba_with_complexity = int(S1*(10**(m*2))+(S3+S4)*(10**(m))+S2) #time complexity n^2
    Karatsuba = int(S1*(10**(m*2))+S6*(10**m)+S2)
#    print (S5)
    print (x,x_H,x_L)
    print (y,y_H,y_L)
    return Karatsuba
print ("result =",karastuba(223245,123456))  