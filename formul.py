count=0
find=0
for i in range(1,2):
    for x in range(3):
        for y in range(3):
            for z in range(3):
                    #print('x^5+'+str(i)+"*x^4+"+str(x)+'*x^3+'+str(y)+"*x^2+"+str(z)+'*x+'+str(w))
                for tou in range(3):
                        #print('x^5+'+str(i)+"*x^4+"+str(x)+'*x^3+'+str(y)+"*x^2+"+str(z)+'*x+'+str(w))
                    a=((i*tou**3)%3+(x*tou**2)%3+(y*tou**1)%3+z)%3
                    #print(a)
                    if a>0:
                        find=find+1
                if find==3:
		            #print('x^5+'+str(l)+'x^4+'+str(r)+'x^3+'+str(x)+'x^2+'+str(y)+'x+'+str(j))
                    print(str(i)+'x^3+'+str(x)+"x^2+"+str(y)+'x+'+str(z))
                    count=count+1
                    find=0
                else:
                    find=0
print(count)
