class Factory:
    def produce(self):
        print("Factory is producing something.")

class Car(Factory):
    def produce(self):
        print("Car factory is producing cars.")

obj = Car()
obj.produce()  # This will call the produce method of the Car class, demonstrating method overriding.