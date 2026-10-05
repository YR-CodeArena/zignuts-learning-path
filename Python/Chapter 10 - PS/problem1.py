class Programmer:
    def __init__(self):
        print("Welcome to Microsoft info desk.")

    def info(self, name, salary, age, language):
        self.name = name
        self.salary = salary
        self.age = age
        self.language = language
        print(f"The name of the programmer is {self.name}. His/Her salary is {self.salary}. His/Her age is {self.age}. And, he/she is currently working on language: {self.language}.")

yash = Programmer()
yash.info("Yash Raval", 1200000, 25, "Python")
