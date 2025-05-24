import os
from pathlib import Path

# r = Read
# a = Append (same thing like update)
# w = Write
# x = Create

# Read - error if it doesn't exist
# f = open("names.txt")
# print(f.read())
# print(f.read(4))

with open("names.txt") as f:
    # print(f.read())

    # print(f.readline())
    # print(f.readline())

    for line in f:
        print(line)

f.close()

print("=======================================")

try:
    f = open("names.txt")
    print(f.read())

except Exception:
    print("The file you want to read does not exist.")

finally:
    f.close()

print("=======================================")

# Append - create the files if it doesn't exist
with open("names.txt", "a") as f:
    f.write("\nJohn Doe")
    f.close()

with open("names.txt") as f:
    print(f.read())
    f.close()

print("=======================================")

# Write (overwrites the file)
with open("context.txt", "w") as f:
    f.write("I deleted all of the context")
    f.close()

with open("context.txt", "r") as f:
    print(f.read())
    f.close()

print("=======================================")

# Two ways to create a new file
# opens a file for writting, creates the file if it does not exist
with open("name_list.txt", "w") as f:
    f.close()
    print("File created")

print("=======================================")

# Creates the specified file, but returns and error if the file exists
if not os.path.exists("riyan.txt"):
    with open("riyan.txt", "x") as f:
        f.close()
        print("File created")

# Delete a file
# avoid an error if it doesn't exist
if os.path.exists("name_list.txt"):
    os.remove("name_list.txt")
    print("File deleted")
else:
    print("The file you want to delete does not exist.")

print("=======================================")
content = Path("more_names.txt").read_text()
print(content)

with open("names.txt", "w") as f:
    f.write(content)
