"""The game() function in  a program lets a user play a game and returns the
score as an integer. you need to read a file "hi-score.txt" which is either blank
or contains the previous hi-score.You need to write a program update hi-score
whenever the game()function breaks the hi-score."""

import random
def game():
    print("You are plying the game...")
    score =  random.randint(1, 62)
    # fetch the hiscore .
    with open ("hiscore.txt")as f:
        hiscore= f.read()
        if hiscore !="" :
            hiscore = int(hiscore)
        else:
            hiscore = 0    
    print(f"your score:{score}")
    if score>hiscore :
    # write this hiscore to the file.
        with open ("hiscore.txt", "w")as f:
            f.write(str(score)) 
    return score

game()

