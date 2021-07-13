str1 = "adw123"
l = list(str1)

for i in range(len(l)):
    if(l[i].isdigit()):
        l[i] = int(l[i])
print(l)



