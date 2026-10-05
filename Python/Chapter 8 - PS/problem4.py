n = int(input("Enter a value: "))
def total(n):
    if(n == 1):
        return 1
    return total(n-1) + n

print(total(n))