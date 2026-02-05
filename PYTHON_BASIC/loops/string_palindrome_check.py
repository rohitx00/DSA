str = input("Enter the string to be checked: ")
str_lower = str.lower()
reversed_str = ""
for ch in str_lower:
    reversed_str = ch + reversed_str
if str_lower == reversed_str:
    print(f"{str} is palindrome")
else:
    print(f"{str} is not a palindrome")