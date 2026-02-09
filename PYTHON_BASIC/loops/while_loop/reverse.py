num = int(input("Enter the number you want to reverse: "))
rev_num = 0

while(num > 0):
    rem = num % 10
    rev_num = rev_num * 10 + rem
    num//=10

print("The reverse number is", rev_num)