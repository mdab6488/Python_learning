# re
# re.search(pattern, string, flags=0)
# re.match(pattern, string, flags=0)
# re.fullmatch(pattern, string, flags=0)
# . any character except a newline
# * 0 or more repetitions
# + 1 or more repetitions
# ? 0 or 1 repetition
# {m} m repetitions
# {m, n} m-n repetitions
# ^ matches the start of the string
# $ matches the end of the string or just before the newline at the end of string
# [] set of characters
# [^] complementing the set
# \d decunal digit
# \D not a decimal digit
# \s whitespace characters
# \S not a whitespace characters
# \w word character as well as numbers the undersocre
# \W not a word character
# A|B either A or B
# (...) a group
# (?:...) non-capturing version

# re.IGNORECASE
# re.MULTILINE
# re.DOTALL

# ^[a-zA-Z0-9.!#$%&'*+\/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9){0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$

import re

print()
email = input("What's your email? ").strip()

# if re.search(r".*@.*", email):
# if re.search(r"..*@..*", email):
# if re.search(r".+@.+", email):
# if re.search(r".+@.+\.edu", email):
# if re.search(r"^.+@.+\.edu$", email):
# if re.search(r"^[^@]+@[^@]+\.edu$", email):
# if re.search(
#         r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.edu$",
#         email):
# if re.search(
#         r"^\w+@\w+\.(com|edu|gov|net|org)$",
#         email,
#         re.IGNORECASE):
# if re.search(
#         r"^(\w|\.)+@(\w+\.)?\w+\.(com|edu|gov|net|org)$",
#         email,
#         re.IGNORECASE):
if re.search(
    r"^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+"
    r"@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?"
    r"(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$",
    email,
    re.IGNORECASE):
    print("Valid Email")
else:
    print("Invalid Email")


