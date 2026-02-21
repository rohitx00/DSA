class Animal:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def __str__(self):
        return f"Animal {self.name} is {self.age} years old."
    
    def __add__(self,other):
        sum = 0
        for i in other:
                sum += i.age
        return self.age + sum

obj = Animal("Dog",10)
obj2 = Animal("Cat",5)
obj3 = Animal("Rabbit",3)
print(obj) # Animal Dog is 10 years old.
print(obj + (obj2, obj3)) 