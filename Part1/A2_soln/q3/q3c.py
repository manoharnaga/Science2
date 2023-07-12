import random
import numpy as np
import matplotlib.pyplot as plt

rollNo = 2021101128

Nmax = 100
Nlist = np.arange(1,101,1,dtype=int)
# print(Nlist)

meanVal = []

for N in Nlist:
    cnt = 0.0
    aVal = []               # Displacement
    for j in range(10000):
        a = 0.0             # Origin
        for i in range(N):
            temp = random.randint(0,1)
            if(temp):
                a += -1
            else:
                a += 1
        aVal.append(a)
    meanVal.append(np.mean(aVal))

# print(meanVal)

plt.xlabel('N')
plt.ylabel('Mean Displacement')
plt.title('N vs Mean Displacement')
plt.plot(Nlist,meanVal)
plt.show()  