# Question 1
import numpy as np
import matplotlib.pyplot as plt


A = np.array([[1,-1,1],[1,-0.5,0.25],[1,0,0],[1,0.5,0.25],[1,1,1]])
A_T = A.transpose()
b = np.array([1,0.5,0,0.5,2])


temp = np.linalg.inv(np.matmul(A_T, A))    # (A^T.A)^-1
temp = np.matmul(temp,A_T)                 # ((A^T.A)^-1).(A^T)
x = np.matmul(temp,b)               # x = ((A^T.A)^-1).(A^T.b)

# print(x)

# plotting the least-squares curve for the data
# p(t) = 1.4t^2+0.4t+0.086

tx = [-1,-0.5,0,0.5,1]
yy = [1,0.5,0,0.5,2]

plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.title('LLS')
x = np.linspace(-1, 1, 150)
y = 1.4 * x**2 + 0.4 * x + 0.086

plt.scatter(tx, yy)
plt.plot(x, y)
plt.show()

