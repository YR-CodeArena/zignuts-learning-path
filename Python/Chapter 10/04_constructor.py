class Employee:
    language = "Python" # This is a class attribute
    salary = 1200000

    def __init__(self, name, salary, language):
        self.name = name
        self.salary = salary
        self.language = language
        print("I am creating an object.")
    
    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    @staticmethod
    def greet():
        print("Good Morning!")

yash = Employee("Yash", 1200000, "JavaScript")
# yash.name = "Yash Raval" # This is an instance attribute
print(yash.name, yash.language, yash.salary)

# rohan = Employee()