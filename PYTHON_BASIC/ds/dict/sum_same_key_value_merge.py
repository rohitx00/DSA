a = {1:20,2:40,3:60,4:80}
b = {4:50,5:100,2:60}

for i in b:
    if i in a.keys():
        a[i] += b[i]
    else:
        a[i] = b[i]

print(a)