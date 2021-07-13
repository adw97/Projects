import numpy as np
"""
arr = np.array([0, 5, 10, 15])

x = [True, False, True, False]

newarr = arr[x]

print(newarr)
"""
arr = np.array([41, 42, 43, 44, 45, 46, 47, 48])

filter_arr = arr % 2 == 0 

newarr = arr[filter_arr]

print(filter_arr)

print(newarr)