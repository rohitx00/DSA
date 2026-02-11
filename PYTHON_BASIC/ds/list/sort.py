a = [23,-19,98,77,11]

n = len(a)
for i in range(n):
    for j in range(0,n-i-1):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
        
    
print("Sorted list is: ",a)