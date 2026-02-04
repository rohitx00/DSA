num = int(input("Enter a number you want to check: "))
if num < 0:
    print("Enter positive numbers only!")
elif num % 2 == 0:
    print(num,"is an even number")
else:
    print(num,"is an odd number")