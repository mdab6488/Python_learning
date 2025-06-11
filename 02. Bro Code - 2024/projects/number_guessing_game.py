import random

lowest_num = 1
heighest_num = 10
answer = random.randint(lowest_num, heighest_num)
guesses = 0
is_running = True

# print(answer)

print("Python Number Gessing Game")
print(f"Select a number between {lowest_num} and {heighest_num}")

while is_running:
    guess = input("Enter your guess: ")
    if guess.isdigit():
        guess = int(guess)
        guesses += 1
        # print(guesses)
        if guess < lowest_num or guess > heighest_num:
            print("That number is out of range ❌")
            print(f"Please select a number between {lowest_num} and {heighest_num}")
        elif guess < answer:
            print("Too low! Try again!")
        elif guess > answer:
            print("Too high! Try again!")
        else:
            print(f"🎉 CORRECT! The answer was {answer}")
            print(f"Number of guesses: {guesses}")
            is_running = False
    else:
        print("Invalid guess ❌")
        print(f"Please select a number between {lowest_num} and {heighest_num}")

