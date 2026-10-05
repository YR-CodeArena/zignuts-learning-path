class Employee:
    
    def __init__(self, salary):
        self.salary = salary
        if self.salary >= 1200000:
            self.increment = (self.salary * 10)/100
        elif self.salary < 1200000:
            self.increment = (self.salary * 20)/100        

    def show(self):
        print(f"The salary of this person is {self.salary} and increment is {self.increment}")
    
    @property
    def salaryAfterIncrement(self):
        return f"{self.salary} + {self.increment} = {self.salary + self.increment}"

    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, value):
        if value <= 0:
            print("Error: Cannot pass zero or negative value as base salary.") 
        else:
            self.salary = value

            if self.salary >= 1200000:
                self.increment = (self.salary * 10)/100
            elif self.salary < 1200000:
                self.increment = (self.salary * 20)/100 

yash = Employee(1300000)
yashvi = Employee(1100000)
yash.salaryAfterIncrement = 1800000
print(yash.salaryAfterIncrement)
yashvi.salaryAfterIncrement = 0
print(yashvi.salaryAfterIncrement)

print("----------")
yash.show()
yashvi.show()
