
import numpy as np


A = np.array([[1, 2, -4], [-2, 1, 3]])

B = np.array([[0, 1, 4], [-1, 3, 1]])

C = np.array([[1, 1], [2, 2]])

D = A * B
E = np.matrix([[1, 2, -1], [3, 1, 0]])
F = np.matrix([[-2, 1], [0, -3], [2, 1]])
print(f'행렬곱 \n{E*F}')   #행렬의 곱


print("A + B =")

print(A + B)   #행렬의 덧셈

print()

print("2*A =")

print(2*A)   #행렬의 스칼라배

print()

print("(-1)*C =")

print((-1)*C)   #행렬의 스칼라배

print(f'행렬 곱 :\n {D}')





