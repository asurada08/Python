import numpy as np

a = np.array([-1, 3, 2, -6])
b = np.array([3, 6, 1, 2])
A = np.reshape(a, [2, 2])
B = np.reshape(b, [2, 2])

print("\n배열 A")
print(A)

print("\n배열 B")
print(B)

result3_1 = np.matmul(A, B)
result3_2 = np.matmul(B, A)

print("\n행렬 result3_1")
print(result3_1)

print("\n행렬 result3_2")
print(result3_2)

b = np.reshape(b, [1, 4])
a = np.reshape(a, [1, 4])
b2 = np.transpose(b)
print(b2)

result = np.matmul(a, b2)
print(result)
