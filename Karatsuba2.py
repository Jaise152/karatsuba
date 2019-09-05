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
    y_H = int(floor(y/10**m))
    y_L = int(y%(10**m))
    openfile = open("outputPS2.txt","a") 
    openfile.writelines("Intermediate Values of A1, B1 after partition" + "\n")
    openfile.writelines("------------------------------------------" + "\n")
    openfile.writelines("A:"+ str(x) + "A1:"+ str(x_H) +"A2:"+ str(x_L)+ "\n")
    openfile.writelines("A:"+ str(y) + "A1:"+ str(y_H) +"A2:"+ str(y_L)+ "\n")
    openfile.close()
    S1 = karastuba(x_H,y_H)
    S2 = karastuba(x_L,y_L)
    S3 = karastuba(x_H,y_L)
    S4 = karastuba(x_L,y_H)
    S5 = karastuba(x_H + x_L , y_H + y_L)
    S6 = S5 - S1 -S2
    Karatsuba_with_complexity = int(S1*(10**(m*2))+(S3+S4)*(10**(m))+S2) #time complexity n^2
    Karatsuba = int(S1*(10**(m*2))+S6*(10**m)+S2)
    return Karatsuba
def readfile(filename):
    f = open(filename, "r")
    f1 = f.readlines()
    x = int(f1[0])
    y = int(f1[1])
    return(x,y)
    
def outputfile():
    openfile = open("outputPS2.txt","a") 
    openfile.writelines("--------Function displayActorsOfMovie --------" + "\n")
    openfile.writelines("Movie name: ")
    openfile.writelines("-----------------------------------------" + "\n")
    openfile.close()
    
    
x = readfile('InputPS2.txt')[0]
y = readfile('InputPs2.txt')[1]
openfile = open("outputPS2.txt","a")
openfile.writelines("1st Number, A :" + str(x) + "\n")
openfile.writelines("1st Number, A :" + str(y) + "\n")
openfile.writelines("------------------------------------------" + "\n")
openfile.close()
#print(x)
#print(y)
openfile = open("outputPS2.txt","a")
openfile.writelines("-----------------------------------------" + "\n")
openfile.writelines("Result:>"+str(x)+"*"+str(y)+"="+ str(karastuba(x,y)))
openfile.close()
