print()

name = input("What's your name? ").capitalize()

# if name == "Riyan":
#     print("Uttara Sector 3")
# elif name == "Alamin":
#     print("ECB")
# elif name == "Anwar" or name == "Rabby":
#     print("Vashantak")
# elif name == "Mim":
#     print("Muksudpur")
# else:
#     print("Who?")

match name:
    case "Riyan":
        print("Uttara Sector 3")
    case "Alamin":
        print("ECB")
    case "Anwar" | "Rabby":
        print("Vashantak")
    case "Mim":
        print("Muksudpur")
    case _:
        print("who?")