import random

num = int(input("Guess the number between 1 - 10: "))

gen_num = random.randint(1,10)

if num == gen_num:
    print(f"Computer choosed {gen_num} and you guessed {num}. You are correct👍")
else:
    print(f"Computer choosed {gen_num} and you guessed {num}. You are incorrect😒")
