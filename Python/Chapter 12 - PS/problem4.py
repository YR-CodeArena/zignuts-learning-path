a = int(input("Enter a number: "))
b = int(input("Enter a second number: "))


if b == 0:
    raise ZeroDivisionError("Infinite")
else:
    result = a/b
    print(result)