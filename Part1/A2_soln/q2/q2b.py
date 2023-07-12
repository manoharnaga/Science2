import random
import numpy as np
import matplotlib.pyplot as plt

# print(2021101128%5+1)

def f(x):
    return np.exp(x)*np.cos(x)          # e^x.cosx

fArr = []

# [-π/2, π/2]
a = -(np.pi/2) 
b =  (np.pi/2)

Nmax = 100000
Nlist = [1,1000]
while(Nlist[-1] < Nmax):
    Nlist.append((Nlist[-1]+1000))

for N in Nlist:
    randArr = np.zeros(N)

    for i in range(N):
        randArr[i] = random.uniform(a,b)

    sumVal = 0.0

    for val in randArr:
        sumVal += f(val)

    integralVal = ((b-a)*sumVal)/float(N)
    fArr.append(integralVal)

plt.xlabel('N')
plt.ylabel('Integral(e^x.cosx)')
plt.title('Integral(e^x.cosx) vs N')
plt.plot(Nlist,fArr)
plt.show()

