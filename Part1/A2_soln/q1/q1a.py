import matplotlib.pyplot as plt
A = 106
C = 1283
M = 6075
N = 1000

I = [0]
index = []

for i in range(1,N+1):
    index.append(i)
    I.append(-1)

I[1] = 1

for j in range(1,N):
    I[j+1] = (A*I[j] + C) % M

plt.xlabel('j')
plt.ylabel('Ij')
plt.title('Ij vs j')
plt.plot(index, I[1:])
plt.show()