import os 
os.system("clear")

from numpy import loadtxt,zeros
from pylab import plot,show

r=int(input("ingrese el valor de r: "))

B=loadtxt("sunspots.txt",float)

x,y=B[:,0],B[:,1]
x1,y1=B[0:1000,0],B[0:1000,1]

x2=B[r:1000,0]

yk=zeros([1000-r],float)
k1=1/(2*r+1)

for i in range(r,1000):
    A=y[(i-r):i+r+1]
    print(A,"\n")
    yk[i-r]=k1*sum(A)


plot(x1,y1)
plot(x2,yk)

show()
