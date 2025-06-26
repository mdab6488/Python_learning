print()

# with open("names.txt", "r") as f:
#     lines = f.readlines()
#
# for line in lines:
#     # print(f" My name is {line}", end="")
#     print(f" My name is {line.rstrip()}")

names = []

with open("names.txt") as f:
    for line in f:
        names.append(line.rstrip())

for name in sorted(names, reverse=False):
    print(f" My name is {name}")

# with open("names.txt") as f:
#     for line in sorted(f):
#         print(f" My name is {line.rstrip()}")
