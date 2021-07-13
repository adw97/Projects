import numpy as np

def binary(n):
    b = bin(n).split("0b")[1]
    a = b.count('1')

    l = list(b)
    revl = l[::-1]

    arr = np.array(revl)
    pos = np.where(arr == '1')

    setb = pos[0]
    lsb = setb[0]
    msb = setb[-1]
    
    output = f"{a}#{lsb}#{msb}"
    return output

n = int(input())
binary = binary(n)
print(binary)



