import random

# def greeting():
#     return "Hi"

# response = greeting()
# print(response)


def get_choices():
    player_choice = input("Enter your choice (rock, paper, scissors): ").lower()

    options = ["rock", "paper", "scissors"]

    return {"player": player_choice, "computer": random.choice(options)}


def check_winner(player, computer):
    print(f"Player chose: {player}\nComputer chose: {computer}")

    if player == computer:
        return "\nIt's a tie!"
    elif player == "rock":
        if computer == "scissors":
            return "\nRock smashes scissors! You wins!"
        else:
            return "\nPaper covers rock! You Loose!"
    elif player == "paper":
        if computer == "scissors":
            return "\nPaper covers rock! You wins!"
        else:
            return "\nscissors cuts paper! You Loose!"
    elif player == "scissors":
        if computer == "paper":
            return "\nScissors cuts paper! You wins!"
        else:
            return "\nRock smashes scissors! You Loose!"


choices = get_choices()
result = check_winner(choices["player"], choices["computer"])
print(result)
