import numpy as np
"""
a = np.array(42)
b = np.array([1, 3, 5, 7, 9])
c = np.array([[1, 3, 5, 7, 9], [2, 4, 6, 8, 10]])
d = np.array([[[1, 3, 5, 7, 9], [2, 4, 6, 8, 10]], [[11, 13, 15, 17, 19], [12, 14, 16, 18, 20]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)
"""
"""
arr = np.array([1, 2, 3, 4, 5], ndmin = 5)

print(arr)
print(f"No. of dimensions: {arr.ndim}")


arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
"""
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(f"Last element from 2nd dim is {arr[1, -1]}")