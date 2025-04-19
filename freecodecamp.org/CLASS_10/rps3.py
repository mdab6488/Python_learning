# value = input("Please enter a value: \n")
# print(value)
import sys
import random
from enum import Enum


def play_rps():
    class RPS(Enum):
        ROCK = 1
        PAPER = 2
        SCISSORS = 3

    playerchoice = input(
        "\nEnter... \n1 for Rock, \n2 for paper or \n3 for scissors: \n\n"
    )

    if playerchoice not in ["1", "2", "3"]:
        print("You must enter 1,2 or 3.")
        return play_rps()

    player = int(playerchoice)

    computerchoice = random.choice([1, 2, 3])

    computer = int(computerchoice)

    print(f"\n you chose {str(RPS(player)).replace('RPS.', '')}.")
    print(f"python chose {str(RPS(computer)).replace('RPS.', '')}.\n")

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

    print("\n Play again?")
    while True:
        playagain = input("\nY for yes or N for no (y/n): ")
        if playagain.lower() not in ["y", "n"]:
            continue
        else:
            break

    # if playagain.lower() == "y":
    #     return play_rps()
    # else:
    #     print("\n 🎉🎉🎉🎉🎉")
    #     print("Thanks for playing! \n")
    #     sys.exit("Bye! 👋")

    if playagain.lower() == "y":
        return play_rps()

    print("\n 🎉🎉🎉🎉🎉")
    print("Thanks for playing! \n")
    sys.exit("Bye! 👋")


play_rps()
