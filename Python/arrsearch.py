import numpy as np

arr = np.array([2, 4, 6, 8])

s = np.searchsorted(arr, [1, 3, 5, 7])

print(s)