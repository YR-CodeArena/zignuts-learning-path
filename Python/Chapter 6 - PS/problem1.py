num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
num3 = int(input("Enter number 3: "))
num4 = int(input("Enter number 4: "))

# Solution 1

# if(num1 - num2 >= 0):
#     if(num1 - num3 >= 0):
#         if(num1 - num4 >= 0):
#             print(num1)
#         else:
#             print(num4)
#     else:
#         if(num3 - num4 >= 0):
#             print(num3)
#         else:
#             print(num4)
        
# elif(num1 - num2 <= 0):
#     if(num2 - num3 >= 0):
#         if(num2 - num4 >= 0):
#             print(num2)
#         else:
#             print(num4)
#     elif(num2 - num3 <= 0):
#         if(num3 - num4 >= 0):
#             print(num3)
#         else:
#             print(num4)

# Solution 2

greatest = num1
if(num2 > greatest):
    greatest = num2
elif(num3 > greatest):
    greatest = num3
elif(num4 > greatest):
    greatest = num4
else:
    print(num1)