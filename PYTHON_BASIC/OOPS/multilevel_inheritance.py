class Car:
    def brand(self,brand):
        self.car_brand = brand
        print(f'Brand of the car is {self.car_brand}')

    def engine(self):
        print("It has 4 * 4 engine")

class Mahindra(Car):
    def __init__(self,name):
        self.name = name
        print(f'Name of the car is {self.name}. ')
    def fuel(self):
        print("It has capacity of 10L")

class SUV700(Mahindra):
    pass

obj = SUV700("SUV700")
obj.brand("Mahindra")
obj.engine()
obj.fuel()