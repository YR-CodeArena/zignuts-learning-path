class Employee:
    language = "Python" # This is a class attribute
    salary = 1200000

    @staticmethod
    def greet():
        print("Good Morning")
    
    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

yash = Employee()
# yash.name = "Yash Raval" # This is an instance attribute
yash.greet()
yash.getInfo()