# Question 4
import numpy as np
import matplotlib.pyplot as plt


A = np.array([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1],[1,-1,0,0],[1,0,0,-1],[0,1,0,-1],[1,0,-1,0],[0,1,-1,0],[0,0,1,-1]])
A_T = A.transpose()
b = np.array([2.95,1.74,-1.45,1.32,1.23,1.61,0.45,4.45,3.21,-2.75])

x = [2.95,1.74,-1.45,1.32]

temp = np.linalg.inv(np.matmul(A_T, A))    # (A^T.A)^-1
temp = np.matmul(temp,A_T)                 # ((A^T.A)^-1).(A^T)
xw = np.matmul(temp,b)               # x = ((A^T.A)^-1).(A^T.b)

print(xw)

# print(x-xw) - difference between computed values and direct measurements


