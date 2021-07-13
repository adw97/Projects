list1 = [64, 34, 25, 12, 22, 11, 90]

#Selection Sort
"""
for i in range(len(list1)):
    for j in range(i+1, len(list1)):
        if(list1[i] > list1[j]):
            list1[i] = list1[i] + list1[j]
            list1[j] = list1[i] - list1[j]
            list1[i] = list1[i] - list1[j]                      
print(list1)
"""

#Bubble Sort
'''
for i in range(len(list1)):
    for j in range(0, len(list1)-1):
        if(list1[j] > list1[j+1]):
            list1[j] = list1[j] + list1[j+1]
            list1[j+1] = list1[j] - list1[j+1]
            list1[j] = list1[j] - list1[j+1]
print(list1)
'''
#Insertion Sort
for i in range(1, len(list1)):
    key = list1[i]
    j = i - 1
    while j >= 0 and key < list1[j]:
        list1[j+1] = list1[j]
        j -= 1
    list1[j+1] = key
print(list1)
    

''' i = 0  j = 1  if(4 > 2) is True, so perform line of code -> list1[0] = 4 + 2 = 6
                                                                list1[1] = 6 - 2 = 4 -->  [2, 4, 12, 8, 9]
                                                                list1[0] = 6 - 4 = 2
           j = 2 if(2 > 12) is False, so line of code will not be executed 

           j = 3 if(2 > 3) is False

           j = 4 if(2 > 9) is False

    i = 1   j = 2 if(4 > 12) is False

            j = 3 if(4 > 3) is True, so perform ->  list1[1] = 7
                                                    list1[3] = 7 - 3 = 4  --> [2, 3, 12, 4, 9]
                                                    list1[1] = 7 - 4 = 3 
            
            j = 4 if(3 > 9) is False

    i = 2   j = 3 if(12 > 4) is True, so perform -> list1[2] = 16
                                                    list1[3] = 16 - 4 = 12  --> [2, 3, 4, 12, 9]
                                                    list1[2] = 16 - 12 = 4

            j = 4 if(4 > 9) is False

    i = 3   j = 4 if(12 > 9) is True, so perform -> list1[3] = 21
                                                    list1[4] = 21 - 9 = 12  --> [2, 3, 4, 9, 12]
                                                    list1[3] = 21 - 12 = 9
    
    i = 4   j = 5, which is out of index so this will not happen

list1 = [2, 3, 4, 9, 12]

Now, we will come out of loop and perform the next line of code
'''


