
def greatest():
    a = int(input("Enter the number: "))
    b = int(input("Enter the number: "))
    c = int(input("Enter the number: "))
    biggest = a
    if(b > a):
        biggest = b
        print("The greatest number is: ", b)
    elif(c > a):
        biggest = c
        print("The greatest number is: ", c)
    else:
        print("The greatest number is:", a)

greatest()