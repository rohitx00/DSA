a = [23,-19,98,77,11]

largest = a[0]
second_largest = a[0]
for num in a:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num

print("Second largest element in the list :",second_largest)