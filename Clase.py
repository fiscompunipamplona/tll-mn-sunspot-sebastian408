import os
os.system("clear")
from numpy import loadtxt
from pylab import plot,show

b=loadtxt("sunspots.txt",float)

x1,y1=b[:,0],b[:,1]
x2,y2=b[0:1000,0],b[0:1000,1]

print("n= ",len(x2))


plot(x1,y1)
show()
plot(x2,y2)


show()
