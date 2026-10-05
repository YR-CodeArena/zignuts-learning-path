n = int(input("Enter a number: "))

def multi(n):
    for i in range(1, 11):
        print(f"{n} X {i} =", n * i)

multi(n)