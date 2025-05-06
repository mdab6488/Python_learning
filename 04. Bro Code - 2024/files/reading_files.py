# Python reading files (.txt, .json, .csv)

# =================================
# .txt
# =================================
# file_path = "C:/Users/LAPTOP GADGET/Desktop/test/output.txt"
#
# try:
#     with open(file_path, "r") as file:
#         content = file.read()
#         print(content)
# except FileNotFoundError:
#     print("That file was not found")
# except PermissionError:
#     print("You do not have permission to read that file")

# =================================
# .json
# =================================
# import json
#
# file_path = "C:/Users/LAPTOP GADGET/Desktop/test/output.json"
#
# try:
#     with open(file_path, "r") as file:
#         content = json.load(file)
#         # print(content)
#         print(content["name"])
# except FileNotFoundError:
#     print("That file was not found")
# except PermissionError:
#     print("You do not have permission to read that file")

# =================================
# .csv
# =================================
import csv

file_path = "C:/Users/LAPTOP GADGET/Desktop/test/output.csv"

try:
    with open(file_path, "r") as file:
        content = csv.reader(file)
        for line in content:
            # print(line)
            print(line[0])
        # print(content)
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You do not have permission to read that file")


