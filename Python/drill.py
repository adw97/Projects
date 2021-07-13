import numpy as np

from numpy import random

Patient_arr = []

i = 0

while i < 5:
    random_no = random.randint(1,100)
    i += 1
    print("Patient's name: ")
    Patient_arr.append(input())
    print(f"Your no. is {random_no}") 
print(Patient_arr)