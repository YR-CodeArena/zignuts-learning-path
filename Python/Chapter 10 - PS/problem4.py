class Calculator:
    def __init__(self):
        print("Welcome to calculator!")
    
    @staticmethod
    def greet():
        print("Hello.")

    def square(self, value):
        self.value = value
        self.result = self.value**2
        print(self.result)
    
    def cube(self, value):
        self.value = value
        self.result = self.value**3
        print(self.result)

    def square_root(self, value):
        self.value = value
        self.result = int(self.value**(1/2))
        print(self.result)

square0 = Calculator()
square0.greet()
square0.square(2)
square0.cube(3)
square0.square_root(9)