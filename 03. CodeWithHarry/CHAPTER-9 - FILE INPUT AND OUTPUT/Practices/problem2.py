import random

print()
def game():
    print("You are playing the game..")
    score = random.randint(a=1, b=62)
    # Fetch the hiscore
    with open("Hi-score.txt", "r") as f:
        hiscore = f.read()
        if hiscore != "":
            hiscore = int(hiscore)
        else:
            hiscore = 0

    print(f"You score: {score}")
    if score > hiscore:
        # write this hiscore to the file
        with open("Hi-score.txt", "w") as f:
            f.write(str(score))

    return score

game()