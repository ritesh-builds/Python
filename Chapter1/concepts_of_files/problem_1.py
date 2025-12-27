import random
def game():
    print("You are playing a game... ")
    score = random.randint(1,100)
    # Fetch high score from a file
    with open("highscore.txt") as f:
        highscore = f.read()
        if (highscore != ''):
            highscore = int(highscore)
        else:
            highscore = 0

    print(f"your score is {score}")
    if(score > highscore):
        # write this score to a file.
        with open("highscore.txt","w") as f:
            f.write(str(score))       
    
    return score 


game()

        
  