class Employee:
    language = "Py" # This is a class attribute
    salary = 1200000

yash = Employee()
yash.name = "Yash Raval"
yash.language = "JavaScript" # This is an instance attribute
print(yash.name, yash.language, yash.salary)