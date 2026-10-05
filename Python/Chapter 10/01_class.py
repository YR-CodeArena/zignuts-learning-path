class Employee:
    language = "Py" # This is a class attribute
    salary = 1200000

yash = Employee()
yash.name = "Yash Raval" # This is an instance attribute
print(yash.name, yash.language, yash.salary)

rohan = Employee()
rohan.name = "Rohan Robinson Roro"
print(rohan.name, rohan.language, rohan.salary)

# Here name is an instance attribute and salary and language are class attributes as they directly belong to the class