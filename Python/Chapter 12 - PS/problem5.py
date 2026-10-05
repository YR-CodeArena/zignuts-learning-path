num = int(input("Enter a number: "))

lst = [num * i for i in range(1, 11)]
with open('Tables.txt', 'a') as f:
    f.write(f"Table of {num}: {str(lst)} \n")
