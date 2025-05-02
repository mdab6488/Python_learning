
questions = ("How many elements are in the periodic table?: ",
             "Which animal lays the largetst egg?: ",
             "What is the most abundant gas in Earth's atmostphere?: ",
             "How many bones are in the human body?: ",
             "Which planet in the solar system is the hottest?: ")

options = (("A. 116","B. 117","C. 118","D. 119"),
           ("A. Whale","B. Crocodile","C. Elephant","D. Ostrich"),
           ("A. Nitrogen","B. Oxygen","C. Carbon-Dioxide","D. Hydrogen"),
           ("A. 206","B. 207","C. 208","D. 209"),
           ("A. Mercury","B. Venus","C. Earth","D. Mars"))

anwsers = ("C", "D", "A", "A", "B")
guesses = []
score = 0
question_number = 0

for question in questions:
    print("-" * 20)
    print(question)
    for option in options[question_number]:
        print(option)

    guess = input("Enter (A, B,C,D): ").upper()
    guesses.append(guess)
    if guess == anwsers[question_number]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{anwsers[question_number]} is the correct answer")

    question_number += 1

print("-" * 20)
print(f"{" " * 7} RESTLTS {" " * 7}")
print("-" * 20)

print("anwsers: ", end="")
for anwser in anwsers:
    print(anwser, end=" ")
print()

print("guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

print("*" * 20)
score = int(score / len(questions) * 100)
print(f"You score is: {score}%")