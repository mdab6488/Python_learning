import random
"""
1 for snake
-1 for water
0 for gun
"""
print()
computer = random.choice(seq=[1, -1, 0])
youstr = input("Enter you choice s/w/g: ").lower()
yourDict = {"s": 1,
            "w": -1,
            "g": 0}
revers_dict = {1: "Snake",
               -1: "Water",
               0: "Gun"}
your_num = yourDict[youstr]

print(f"You chose '{revers_dict[your_num]}'\nComputer choose '{revers_dict[computer]}'")

print("*" * 30)
# computer ==-1
if computer == your_num:
    print("It's Draw! 👍")
else:
    # if computer == -1 and your_num == 1: # -2
    #     print("You win! 😍")
    # elif computer == -1 and your_num == 0: # -1
    #     print("You win! 😍")
    #
    # # computer == 1
    # elif computer == 1 and your_num == -1: # 2
    #     print("You loose! 🙃")
    # elif computer == 1 and your_num == 0: # 1
    #     print("You win! 😍")
    #
    # # computer == 0
    # elif computer == 0 and your_num == 1: # 1
    #     print("You loose! 🙃")
    # elif computer == 0 and your_num == -1: # 1
    #     print("You win! 😍")
    # else:
    #     print("Something Wrong")

    if computer - your_num  == -1 or computer - your_num == 2:
        print("You loose! 🙃")
    else:
        print("You win! 😍")

print("*" * 30)