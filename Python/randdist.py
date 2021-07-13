from numpy import random

x = random.choice([5, 10, 15, 20], p = [0.1, 0.3, 0.6, 0], size = (5,5))

print(x)