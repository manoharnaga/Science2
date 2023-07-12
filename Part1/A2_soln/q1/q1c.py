import numpy as np
import matplotlib.pyplot as plt

A = 106
C = 1283
M = 6075

Nmax = 2000
Nlist = [1,10,50,100]
while(Nlist[-1] < Nmax):
    Nlist.append((Nlist[-1]+100))

# print(Nlist)

MeanArr = []

for N in Nlist:
    I = np.zeros(N+1)
    I[1] = 1
    for j in range(1,N):
        I[j+1] = (A*I[j] + C) % M

    I = np.delete(I,0)
    MeanVal = np.mean(I)
    MeanArr.append(MeanVal)

plt.xlabel('N')
plt.ylabel('E(Ij)')
plt.title('E(Ij) vs N')
plt.plot(Nlist,MeanArr)
plt.show()