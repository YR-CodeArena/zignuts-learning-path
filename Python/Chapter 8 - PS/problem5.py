n = int(input("Enter a value: "))
def pattern(n):
    for i in range(n, 0, -1):
        print("*" * i, end="")
        print("")

pattern(n)