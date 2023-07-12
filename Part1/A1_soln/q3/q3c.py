import numpy as np
import matplotlib.pyplot as plt

                            #Real And Symmetric

mu = 0
sigma = 1
n = 500
s = np.random.normal(mu, sigma, n*n)
A = np.reshape(s,(n,n))

D = [0,1,5,10]

plotx = []
ploty = []

for val in D:
    for i in range(len(A)):
        for j in range(len(A[0])):
            if(i == j):
                A[i][j] = -val
    #Real And Symmetric
    for i in range(len(A)):
        for j in range(len(A[0])):
                A[j][i] = A[i][j]
    #Real And Symmetric
    eigVals = np.linalg.eigvals(A)
    realX = eigVals.real
    imagY = eigVals.imag
    plotx.append(realX)
    ploty.append(imagY)

colorArr = ['red','blue','green','violet']

plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.title('Real(lambda) vs Imag(lambda)')
for i in range(len(plotx)):
    plt.scatter(plotx[i], ploty[i],color=colorArr[i])

plt.show()