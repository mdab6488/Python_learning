# value = input("Please enter a value: \n")
# print(value)
import sys
import random
from enum import Enum


class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


playagain = True

while playagain:
    # print(RPS(2))
    # print(RPS.ROCK)
    # print(RPS["ROCK"])
    # print(RPS.ROCK.value)
    # sys.exit()

    playerchoice = input(
        "\nEnter... \n1 for Rock, \n2 for paper or \n3 for scissors: \n\n"
    )

    player = int(playerchoice)

    if player < 1 or player > 3:
        sys.exit("You must enter 1,2 or 3.")

    computerchoice = random.choice([1, 2, 3])

    computer = int(computerchoice)

    # print("you chose " + playerchoice + ".")

    # print(f"you chose {playerchoice}.")
    # print(f"python chose {computerchoice}.")
    print(f"\n you chose {str(RPS(player)).replace('RPS.', '')}.")
    print(f"python chose {str(RPS(computer)).replace('RPS.', '')}.\n")

    # if player == 1 and computer == 3:
    #     print("🎉 You win! ")
    # elif player == 2 and computer == 1:
    #     print("🎉 You win! ")
    # elif player == 3 and computer == 2:
    #     print("🎉 You win! ")
    # elif player == computer:
    #     print("😲 It's a tie!")
    # else:
    #     print("🐍 Python wins!")

    if (
        (player == 1 and computer == 3)
        or (player == 2 and computer == 1)
        or (player == 3 and computer == 2)
    ):
        print("🎉 You win! ")
    elif player == computer:
        print("😲 It's a tie!")
    else:
        print("🐍 Python wins!")

    playagain = input("Do you want to play again? (y/n): ")

    if playagain.lower() == "y":
        continue
    else:
        print("\n 🎉🎉🎉🎉🎉")
        print("Thanks for playing! \n")
        playagain = False
        # break

sys.exit("Bye! 👋")
