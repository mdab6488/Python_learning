import random

options = ("rock", "paper", "scissors")

playing = True

while playing:
    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Enter a choice (rock, paper, scissors): ")

    print(f"Player: {player}")
    print(f"Compute: {computer}")

    if player == computer:
        print("It's a tie!")
    elif player == "rock" and computer == "scissors" or player == "paper" and computer == "rock" or player == "scissors" and computer == "paper":
        print("You win! 🎉")
    else:
        print("You lose! 🥲")

    # play_again = input("Playt again? (y/n): ").lower()
    # if not play_again == "y":
    #     playing = False

    if not input("Playt again? (y/n): ").lower() == "y":
        playing = False

print("Thanks for playing!")