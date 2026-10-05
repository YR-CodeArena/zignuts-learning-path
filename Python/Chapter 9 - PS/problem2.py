import random
def game():    
    i = "yes"
    highscore = 0
    while i == "yes":
        a = random.randint(1, 100)
        b = random.randint(1, 100)
        print("Your numbers are: ", a, b)
        total = int(input("The sum of these numbers would be: "))
        
        if total == a + b:
            highscore += 1           
            print("Highscore is: ", highscore)
        else:
            print("Highscore is: ", highscore)
            
        i = input("Do you want to play again? yes or no? ")
    with open("Hi-score.txt", "w") as f:
        hs = str(highscore)
        f.write(hs)
    
game()
