import random

print("Let's play Snake, Water and Gun!")
print("Enter 1 for Snake, 0 for Water and -1 for Gun:")
player = int(input("Enter your choice: "))
choices = [-1, 0, 1]
computer = random.choice(choices)

name = {-1 : "Gun", 1 : "Snake", 0 : "Water"}

p = name[player]
c = name[computer]

if((player == 1 and computer == 0) or (player == 0 and computer == -1) or (player == -1 and computer == 1)):
    print("You win!")
    print(f"You chose: {player}, which is {p} and Computer chose: {computer}, which is {c}")
elif(player == computer):
    print("Game draw!")
    print(f"You chose: {player}, which is {p} and Computer chose: {computer}, which is {c}")
else:
    print("You lose, computer wins!")
    print(f"You chose: {player}, which is {p} and Computer chose: {computer}, which is {c}")
