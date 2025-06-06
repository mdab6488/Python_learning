from wordlist import words
import random



#dictionary of a key:()
handman_art = {
    0: ("   ",
        "   ",
        "   "),
    1: (" o ",
        "   ",
        "   "),
    2: (" o ",
        " | ",
        "   "),
    3: (" o ",
        "/| ",
        "   "),
    4: (" o ",
        "/|\\",
        "   "),
    5: (" o ",
        "/|\\",
        "/  "),
    6: (" o ",
        "/|\\",
        "/ \\"),
}

# print(handman_art[0])
# for line in handman_art[6]:
#     print(line)

def display_man(wrong_guesses):
    print("*" * 30)
    for line in handman_art[wrong_guesses]:
        print(line)
    print("*" * 30)

def display_hint(hint):
    print(" ".join(hint))

def display_anwser(anwser):
    print(" ".join(anwser))

def main():
    answer = random.choice(words)
    # print(answer)

    hint = ["_"] * len(answer)
    # print(hint)

    wrong_guesses = 0
    guessed_letters = set()
    is_running = True

    while is_running:
        display_man(wrong_guesses)
        display_hint(hint)
        # display_anwser(answer)
        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid Input")
            continue

        if guess in guessed_letters:
            print(f"{guess} is already guessed")
            continue

        guessed_letters.add(guess)

        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
        else:
            wrong_guesses += 1

        if "_" not in hint:
            display_man(wrong_guesses)
            display_anwser(answer)
            print("YOU WIN!")
            is_running = False
        elif wrong_guesses >= len(handman_art) - 1:
            display_man(wrong_guesses)
            display_anwser(answer)
            print("YOU LOSE!")
            is_running = False


if __name__ == '__main__':
    main()