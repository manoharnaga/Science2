import random
import numpy as np

# print(2021101128%5+1)

N = 100000
def f(x):
    return np.exp(x)*np.cos(x)          # e^x.cosx

# [-π/2, π/2]
a = -(np.pi/2) 
b =  (np.pi/2)

randArr = np.zeros(N)

for i in range(N):
    randArr[i] = random.uniform(a,b)

sumVal = 0.0

for val in randArr:
    sumVal += f(val)

integralVal = ((b-a)*sumVal)/float(N)

print(integralVal)


