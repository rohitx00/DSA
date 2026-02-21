class Car:
    def fly(self):
        print("Car is flying!")

class Airplane:
    def fly(self):
        print("Airplane is flying!")

obj = Car()
obj2 = Airplane()
obj.fly()  # This will call the fly method of the Car class
obj2.fly()  # This will call the fly method of the Airplane class