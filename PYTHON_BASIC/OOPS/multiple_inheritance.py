class Father:
    def __init__(self,name,job):
        self.job = job
        self.name = name
        print(f'my name is {self.name} and job is {self.job}')

class Mother:
    def __init__(self,name):
        self.name = name
        print(f"My name is {self.name}")

class Son(Mother,Father):
    pass

obj = Son("Rohit")