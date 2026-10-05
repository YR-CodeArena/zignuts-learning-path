n = int(input("Enter a number: "))

print("*" * n)
s = " " * (n-2)
for i in range(2, n):
    print(f"*{s}*")
print("*" * n)
