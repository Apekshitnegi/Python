import random

def game():
    print("you are playing game...")
    score = random.randint(1,62)

    with open (r"c:\Users\Apekshit negi\OneDrive\Documents\Desktop\Python\Chapter 9\Practice question\hiscore.txt") as f :
        hiscore = f.read()
        if ( hiscore != ""):
            hiscore = int(hiscore)
        else:
            hiscore = 0

    print(f"your hiscore {score}")
    if(score>hiscore):
      with open (r"c:\Users\Apekshit negi\OneDrive\Documents\Desktop\Python\Chapter 9\Practice question\hiscore.txt", "w") as f:
          f.write(str(score))
    return score

game()
          