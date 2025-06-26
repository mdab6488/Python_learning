# docs.python.org/3/library/functions.html#open

print()
name = input("What's your name? ")

with open("names.txt", "a") as f:
    f.write(f"{name}\n")
