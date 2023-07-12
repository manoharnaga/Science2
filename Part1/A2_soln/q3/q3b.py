import random
import numpy as np
import matplotlib.pyplot as plt

rollNo = 2021101128

Nmax = 100
Nlist = np.arange(1,101,1,dtype=int)
# print(Nlist)

probVal = []

for N in Nlist:
    cnt = 0.0
    for j in range(10000):
        a = -(rollNo%5 + 1)
        b =  (rollNo%5 + 1)
        for i in range(N):
            temp1 = random.randint(0,1)
            temp2 = random.randint(0,1)
            if(temp1):
                a += -1
            else:
                a += 1

            if(temp2):
                b += -1
            else:
                b += 1

        if(a==b):
            cnt += 1.0
    probVal.append((cnt/10000))

# print(probVal)

plt.xlabel('N')
plt.ylabel('probability')
plt.title('N vs probability')
plt.plot(Nlist,probVal)
plt.show()  