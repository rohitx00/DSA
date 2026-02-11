a = [2,9,-1,-8,10,3,-15]
positive = []
negative = []
for num in a:
    if num > 0:
        positive.append(num)
    else:
        negative.append(num)

for num in positive:
    print(num, end=", ")

print()

for num in negative:
    print(num, end=", ")