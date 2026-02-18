class Factory:
    def __init__(self, name):
        self.name = name

    def produce(self):
        print(f"{self.name} is producing something.")

class Car(Factory):
    def __init__(self, name, model):
        super().__init__(name)
        self.model = model

    def display_info(self):
        print(f"{self.name} produces {self.model} cars.")

class Bike(Factory):
    def __init__(self, name, type):
        super().__init__(name)
        self.type = type

    def display_info(self):
        print(f"{self.name} produces {self.type} bikes.")

car_factory = Car("Toyota", "Corolla")
bike_factory = Bike("Honda", "CBR")
car_factory.produce()
car_factory.display_info()  
bike_factory.produce()
bike_factory.display_info()