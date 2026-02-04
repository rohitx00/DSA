temperature = int(input("Enter the tempreture: "))
if temperature < 0:
    print("Freezing cold")

elif temperature >=0 and temperature < 10:
    print("Very cold")

elif temperature >= 10 and temperature < 20:
    print("Cold")

elif temperature >= 20 and temperature < 30:
    print("Pleasant")

elif temperature >=30 and temperature < 40:
    print("Hot")

else:
    print("Very hot")