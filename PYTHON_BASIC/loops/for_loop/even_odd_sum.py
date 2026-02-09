num = int(input("Enter the range: "))
even_sum = 0
odd_sum = 0
for i in range(1, num+1):
    if i % 2 == 0:
        even_sum += i
    else:
        odd_sum += i

print(f"The sum of the even number is {even_sum}")
print(f"The sum of the odd number is {odd_sum}")
