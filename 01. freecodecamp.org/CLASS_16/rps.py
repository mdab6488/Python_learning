# value = input("Please enter a value: \n")
# print(value)
import sys
import random
from enum import Enum


def rps(name="PlayerOne"):
    game_count = 0
    payer_wins = 0
    python_wins = 0

    def play_rps():
        nonlocal name, payer_wins, python_wins

        class RPS(Enum):
            ROCK = 1
            PAPER = 2
            SCISSORS = 3

        playerchoice = input(
            f"\n{name} Please enter... \n1 for Rock, \n2 for paper or \n3 for scissors: \n\n"
        )

        if playerchoice not in ["1", "2", "3"]:
            print(f"{name}, please enter 1,2 or 3.")
            return play_rps()

        player = int(playerchoice)

        print("--------------------------------------------")

        computerchoice = random.choice([1, 2, 3])

        computer = int(computerchoice)

        print(f"{name} chose {str(RPS(player)).replace('RPS.', '').title()}.")
        print(f"python chose {str(RPS(computer)).replace('RPS.', '').title()}.\n")

        def decided_winner(player, computer):
            nonlocal payer_wins, python_wins
            if (
                (player == 1 and computer == 3)
                or (player == 2 and computer == 1)
                or (player == 3 and computer == 2)
            ):
                payer_wins += 1
                return f"🎉 {name}, win! "
            elif player == computer:
                return "😲 It's a tie!"
            else:
                python_wins += 1
                return f"🐍 Python wins!\n,Sorry, {name}...🥲"

        game_result = decided_winner(player, computer)
        print(game_result)

        print("--------------------------------------------")

        nonlocal game_count
        game_count += 1
        print(f"Games played: {game_count}")
        print(f"{name}'s wins: {payer_wins}")
        print(f"Python wins: {python_wins}")

        print("--------------------------------------------")

        print(f"Play again, {name}")
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

        # if playagain.lower() == "y":
        #     return play_rps()
        # else:
        #     print("\n 🎉🎉🎉🎉🎉")
        #     print("Thanks for playing! \n")
        #     if __name__ == "__main__":
        #         sys.exit(f"Bye! {name} 👋")
        #     else:
        #         return

        if playagain.lower() == "y":
            return play_rps()

        print("\n 🎉🎉🎉🎉🎉")
        print("Thanks for playing! \n")
        if __name__ == "__main__":
            sys.exit(f"Bye! {name} 👋")
        return

    return play_rps


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Provides a personal game experience.")

    parser.add_argument(
        "-n",
        "--name",
        metavar="name",
        required=True,
        help="The name of the person playing the game.",
    )
    args = parser.parse_args()

    rock_paper_scissors = rps(args.name)
    rock_paper_scissors()
