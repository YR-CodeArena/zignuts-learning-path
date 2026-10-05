username = input("Enter your username: ")

if(len(username) < 10):
    print("Total number of characters are less than 10.")
elif(len(username) >= 10):
    print("Total number of characters are 10 or more.")