a = [23,-19,98,77,11]
max = a[0]
index = 0

for i in range(1,len(a)):
    if a[i] > max:
        max = a[i]
        index = i
    
print("The index of the greatest element is :", index)
print("Greatest element is :", max)