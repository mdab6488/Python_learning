# value = input("Please enter a value: \n")
# print(value)
import sys
import random
from enum import Enum


def res():
    game_count = 0
    payer_wins = 0
    python_wins = 0

    def play_rps():
        nonlocal payer_wins, python_wins

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

        print(f"\n you chose {str(RPS(player)).replace('RPS.', '').title()}.")
        print(f"python chose {str(RPS(computer)).replace('RPS.', '').title()}.\n")

        def decided_winner(player, computer):
            nonlocal payer_wins, python_wins
            if (
                (player == 1 and computer == 3)
                or (player == 2 and computer == 1)
                or (player == 3 and computer == 2)
            ):
                payer_wins += 1
                return "🎉 You win! "
            elif player == computer:
                return "😲 It's a tie!"
            else:
                python_wins += 1
                return "🐍 Python wins!"

        game_result = decided_winner(player, computer)
        print(game_result)

        nonlocal game_count
        game_count += 1
        print(f"\nGames played: {game_count}")
        print(f"\nPlayer wins: {payer_wins}")
        print(f"\nPython wins: {python_wins}")

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

    return play_rps


rock_paper_scissors = res()

if __name__ == "__main__":
    rock_paper_scissors()
