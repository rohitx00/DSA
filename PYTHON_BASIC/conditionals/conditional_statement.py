age = int(input("Enter your age: "))

if age < 0 or age > 102:
    print("Enter a valid age")

else:

    if age >= 18:
        print("You can vote")

    else:
        print("You can't vote")

