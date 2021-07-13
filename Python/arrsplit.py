import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])

newarr = np.dsplit(arr, 3)

print(newarr)