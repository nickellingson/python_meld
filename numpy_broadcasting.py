import numpy as np

# Example, if a.shape is (5,1), 
# b.shape is (1,6), c.shape is (6,) and d.shape is () so that d is a scalar

# a = np.array([[3], [3], [3], [3], [3], [3]])
a = np.arange(5).reshape(5, 1)
print(a)
print(a.shape)
print(a.ndim)

b = np.array([np.ones(6)])
print(b)
print(b.shape)
print(b.ndim)

c = np.arange(6)
print(c)
print(c.shape)
print(c.ndim)

d = 10

# matmul
result1 = a @ b
print(result1)
print(result1.shape)
print(result1.ndim)

result2 = b @ c
print(result2)
print(result2.shape)
print(result2.ndim)

result3 = a * d
print(result3)
print(result3.shape)
print(result3.ndim)
