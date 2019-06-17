import pandas as pd
import os
import random as rd
import numpy as np
import matplotlib.pyplot as plt

def generate_table():
    a=pd.DataFrame({"values":createvalue()}, index=pd.date_range("1/1/1993", periods=30, freq="Y"))
    #d=pd.read_excel('rs.xlsx')
    #print(d)
    #d=d.interpolate(method='index',xis=0,iplace=True)
    #df=mt.figure(a)
    a=a.interpolate(method='index',xis=0,iplace=True)
    print(a)
    x=a.index.array
    y=[(a.values[i]) for i in range(30)]
    plt.plot(x,y)
    plt.ylabel('y')
    plt.xlabel('x')
    plt.show()

def createvalue():
    a=[]
    value=100
    trigger=True
    for i in range(30):
        if i<4:
            value=+rd.randint(100,150)
        elif i==4:
            value=1000
        elif i>4 and i<(4+3):
            value=value-rd.randint(0,300)
        elif i>=7 and i<17:
            value=value+rd.randint(850,1200)
        elif i>=17 and i<20:
            value=np.nan#-=rd.randint(0,2000)
        elif i>=20 and i<30:
            value=rd.randint(50,6000)#np.nan
        #print(value)
        a.append((value))
    return a
def main():
    generate_table()

if __name__=='__main__':
    main()
    exit()
