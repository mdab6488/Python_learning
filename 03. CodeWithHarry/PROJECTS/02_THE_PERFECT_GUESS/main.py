import random

n = random.randint(1, 20)
a = -1
guesses = 1

while a != n:
    a = int(input("Guess a number: "))

    if a > n:
        print("Lower Number Please")
        guesses += 1
    elif a < n:
        print("Higher Number Please")
        guesses += 1

print(f"You have guessed the number {n} correctly in {guesses} attempts")