a = [23,-19,98,77,11]

for num in range(len(a)):
    if a[num] < a[num+1]:
        continue
    else:
        print("List is not sorted")
        break
else:
    print("Your list is sorted")