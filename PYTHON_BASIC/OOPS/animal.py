class Animal:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def show(self):
        print(f'I am {self.name} and my age is {self.age}')
    
    @classmethod
    def hello(cls):
        print("This is the class method")

    @staticmethod
    def static():
        print("This is the static method")

obj = Animal("Tommy", 7)
obj.show()
        