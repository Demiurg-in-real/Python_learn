import pandas as pd
import numpy as np
import os
import random
def main(asd):
    print(asd)
    case={ "1" : mktable(), "99": "Test is successfull!", "2":geti()}
    print(case.get(asd))

def geti():
    a=createtable()
    return a#.loc[4:9,['dates','e','r']]#a.describe()#a.to_numpy() - smtimes helpful#a.columns#a.index#a.tail(2)#a.head()#a.dtypes
def mktable():
    Ok = 21
    #df=pd.Series([1,4,5,23,np.nan,Ok]) it is just for column-make
    dataS=pd.date_range('19990902',periods=6)
#    for i in range(0,10):
#        dataS.append(random.randint(1,99))
    df=pd.DataFrame(np.random.randn(6,4),index=dataS,columns=list('ABCD'))#dict[1:1,2:23,3:11,4:os.urandom(2)]) - dict is not working here
    return df
    #print(dataS)

def createtable():
    dates=pd.date_range(start='1999',periods=11,freq="Y")
    df1=pd.DataFrame({ 'Numders' : [os.urandom(1) for i in range(11)], 'dates':pd.Timestamp('19720101'),'c':pd.Series(1,index=(range(11)),dtype='float32'), 'd':np.array([3]*11,dtype='int32'),'e': pd.Categorical(['I','want','coding','.','Hard','coding','with','notebook','and','hardcore','!']),'r':dates}, index=dates)
    return df1 #arrays(columns) must have the same length and one cell can't contain more than one element(don't use arrays)
if __name__=='__main__':
    main(str(input()))
    exit()
