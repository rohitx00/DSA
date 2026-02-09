num = int(input("Enter the number you want to check: "))

check_num = num
rev_num = 0

while(num > 0):
    rem = num % 10
    rev_num = rev_num * 10 + rem
    num//=10

if check_num == rev_num:
    print(f"{num} is Palindrome")
else:
    print(f"{num} is not a palindrome")