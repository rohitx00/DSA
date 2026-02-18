class Car:
    def engine(self):
        print("Car needs engine to run")
    def wheels(self):
        print("Car have four wheels")
    
class Dzire(Car):
    def color(self,color):
        self.color = color
        print(f"Color is {self.color}")

obj = Dzire()
obj.color("White")
obj.engine()