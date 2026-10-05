import random

ran = random.randint(1, 100)
guess = int(input("Enter the number you are guessing: "))

count = 1
while guess != ran:
    if guess > ran:
        print("Lower Number Please.")
        guess = int(input("Enter the number you are guessing: "))
        count += 1
    elif guess < ran:
        print("Higher Number Please.")
        guess = int(input("Enter the number you are guessing: "))
        count += 1
if guess == ran:
    print(f"Total steps to guess the number: {count}")    
