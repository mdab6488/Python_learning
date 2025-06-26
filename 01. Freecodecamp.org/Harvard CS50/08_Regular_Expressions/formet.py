import re

# A|B either A or B
# (...) a group
# (?:...) non-capturing version

print()
name = input("What's your name? ").strip()

# if "," in name:
#     first, last = name.split(", ")
#     name = f"{first} {last}"
# print(f"hello, {name}")

# matches = re.search(
#     pattern=r"^(.+), *(.+)$",
#     string=name)
# if matches:
#     # last, first = matches.groups()
#     # name = f"{first} {last}"
#     name = matches.group(2) + " " + matches.group(1)

if matches := re.search(r"^(.+), *(.+)$", name):
    name = matches.group(2) + " " + matches.group(1)
print(f"hello, {name}")
