import json
import random
from pathlib import Path


class Bank:
    database = Path("data.json")
    data = []

    # -------- Load Database --------
    if database.exists():
        try:
            with open(database, "r") as f:
                data = json.load(f)
        except:
            data = []

    # -------- Save Database --------
    @staticmethod
    def update():
        with open(Bank.database, "w") as f:
            json.dump(Bank.data, f, indent=4)

    # -------- Generate Unique Account --------
    @classmethod
    def __generate_account(cls):
        while True:
            num = random.randint(1000000, 9999999)
            if not any(acc["account_no"] == num for acc in cls.data):
                return num

    # -------- Find User --------
    @staticmethod
    def __find_user(acc_no, pin):
        for user in Bank.data:
            if user["account_no"] == acc_no and user["pin"] == pin:
                return user
        return None

    # -------- Create Account --------
    def create_account(self, name, age, email, pin):
        if age < 18:
            return "Age must be 18+"

        if len(str(pin)) != 4:
            return "PIN must be 4 digits"

        user = {
            "name": name,
            "age": age,
            "email": email,
            "pin": pin,
            "account_no": Bank.__generate_account(),
            "balance": 0
        }

        Bank.data.append(user)
        Bank.update()
        return user

    # -------- Deposit --------
    def deposit(self, acc_no, pin, amount):
        user = self.__find_user(acc_no, pin)
        if not user:
            return "Invalid credentials"

        if amount <= 0 or amount > 100000:
            return "Invalid deposit amount"

        user["balance"] += amount
        Bank.update()
        return user["balance"]

    # -------- Withdraw --------
    def withdraw(self, acc_no, pin, amount):
        user = self.__find_user(acc_no, pin)
        if not user:
            return "Invalid credentials"

        if amount > user["balance"]:
            return "Insufficient balance"

        user["balance"] -= amount
        Bank.update()
        return user["balance"]

    # -------- Details --------
    def details(self, acc_no, pin):
        user = self.__find_user(acc_no, pin)
        if not user:
            return None
        return user

    # -------- Update --------
    def update_details(self, acc_no, pin, name=None, email=None, new_pin=None):
        user = self.__find_user(acc_no, pin)
        if not user:
            return "Invalid credentials"

        if name:
            user["name"] = name
        if email:
            user["email"] = email
        if new_pin:
            if len(str(new_pin)) != 4:
                return "PIN must be 4 digits"
            user["pin"] = int(new_pin)

        Bank.update()
        return "Updated successfully"

    # -------- Delete --------
    def delete(self, acc_no, pin):
        user = self.__find_user(acc_no, pin)
        if not user:
            return "Invalid credentials"

        Bank.data.remove(user)
        Bank.update()
        return "Account deleted"