'''
Name: Rajiv Das
Reg.: 2015 132 036
'''

'''I used equations from this PDF(link given below)---
   https://www.mn.uio.no/ifi/english/services/knowledge/cs/forelesn.kap5.pdf'''


'''This program takes some data points and then it calculates the
   equation of trendline by Least Square Method'''


import matplotlib.pyplot as pl
x=[] #Declearing the list for X values#
y=[] #Declearing the list for Y values#
p=int(input("Enter the number of points you want to input:"))


print("Enter X values from data :")
i=0
while(i<p):#Loop for putting the X values in the appropriate list#
    o=float(input())
    x.append(o)
    i=i+1


print("Enter Y values from data:")
i=0
while(i<p):#Loop for putting the Y values in the appropriate list#
    q=float(input())
    y.append(q)
    i=i+1


print("Data points are:")
i=0
while(i<p):#Loop for showing the data points from input#
    print("(x,y)=({},{}) ".format(x[i],y[i]))
    i=i+1


i=0
c1=0
while(i<p):#Loop for calculating c1(sum of X values)#
    c1=c1+x[i]
    i=i+1
print("c1 is {}".format(c1))


i=0
c2=0
while(i<p):#Loop for calculating c2(sum of X squared values)#
    c2=c2+(x[i]*x[i])
    i=i+1
print("c2 is {}".format(c2))


i=0
c3=0
while(i<p):#Loop for calculating c3(sum of Y values)#
    c3=c3+y[i]
    i=i+1
print("c3 is {}".format(c3))


i=0
c4=0
while(i<p):#Loop for calculating c4(sum of X multiplied by Y )#
    c4=c4+(x[i]*y[i])
    i=i+1
print("c4 is {}".format(c4))


a0=(c2*c3-c1*c4)/(p*c2-c1*c1)#calculating interception of the trendline at Y axis as a0#
print("a0 is {}".format(a0))


a1=(p*c4-c1*c3)/(p*c2-c1*c1)#Calculating slope of the trendline as a1#
print("a1 is {}".format(a1))


'''Trendline plot'''
X=[min(x),max(x)]#A list for ploting trendline#
Y=[]#A list for Y values of trendline from equation y=a0+a1*x#


i=0
while(i<2):#Loop for calculating Y values from equation y=a0+a1*x#
    z=a0+a1*X[i]
    Y.append(z)
    i=i+1

#Rounding a0 and a1 for graph's title#
na0=round(a0,2)
na1=round(a1,2)


pl.plot(x,y,'ro')#For showing data(from input) points on plot#
pl.plot(X,Y,'k')#For showing trendline on plot#
pl.xlabel("X values")
pl.ylabel("Y values")
pl.title("Equation of the trendline is \n y=({})x+({})".format(na1,na0))
pl.show()