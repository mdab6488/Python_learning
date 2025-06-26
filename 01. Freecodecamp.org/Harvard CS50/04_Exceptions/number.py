print()

# try
# except
# else

# try:
#     x = int(input("What's x? ")) # alamin # ValueError
# except ValueError:
#     print(f"x is not integer")
# else:
#     print(f"x is {x}")

# while True:
#     try:
#         x = int(input("What's x? ")) # alamin # ValueError
#     except ValueError:
#         print(f"x is not integer Try again.")
#     else:
#         break
#
# print(f"x is {x}")

# def main():
#     x = get_int()
#     print(f"x is {x}")

# def get_int():
#     while True:
#         try:
#             number = int(input("What's x? "))  # alamin # ValueError
#         except ValueError:
#             print(f"x is not integer Try again.")
#         else:
#             return number

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))  # alamin # ValueError
        except ValueError:
            print(f"x is not integer Try again?")
            # pass

# main()

if __name__ == "__main__":
    x = get_int("What's x? ")
    print(f"x is {x}")