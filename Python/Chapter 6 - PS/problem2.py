maths = int(input("Enter your maths marks: "))
ml = int(input("Enter your ml marks: "))
ai = int(input("Enter your ai marks: "))

percentage = ((maths + ml + ai) * 100) / 300
print(percentage)

if(percentage >= 40 and ml >= 33 and ai >= 33 and maths >= 33):
    print("Congratulations! You have passed!")
else:
    print("Sorry, you have failed.")