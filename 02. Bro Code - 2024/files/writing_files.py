# Python writing files (.txt .json, .csv)

# ========================
# .txt
# ========================
# txt_data = "I like pizza!"
# file_path = "output.txt"
#
# with open(file=file_path, mode="w") as file:
#     file.write(txt_data)
#     print(f"txt file '{file_path}' was created")

# employees = ["Eugene", "Squidward", "Spongebob", "Patrick"]
#
# # txt_data = "I like pizza!"
# file_path = "C:/Users/LAPTOP GADGET/Desktop/test/output.txt"
#
# try:
#     with open(file=file_path, mode="a") as file:
#         # file.write("\n" + txt_data)
#         for employee in employees:
#             file.write("\n" + employee)
#         print(f"txt file '{file_path}' was created")
# except FileExistsError:
#     print(f"That file already exists!")
# except TypeError:
#     print()

# ========================
# .json
# ========================
# {
#     "firstName": "Joe",
#     "lastName": "Jackson",
#     "gender": "male",
#     "age": 28,
#     "address": {
#         "streetAddress": "101",
#         "City": "San Diego",
#         "State": "CA"
#     },
#     "phoneNumber": [
#         {
#             "type": "home",
#             "number": "01900000000"
#         }
#     ]
# }

import json

employee = {
    "name": "Spongebob",
    "age": 30,
    "job": "cook"
}

file_path = "C:/Users/LAPTOP GADGET/Desktop/test/output.json"

try:
    with open(file=file_path, mode="w") as file:
        json.dump(employee, file, indent=4)
        print(f"json file '{file_path}' was created")
except FileExistsError:
    print(f"That file already exists!")
except TypeError:
    print()


# ========================
# .csv
# ========================
# Report generate on 01-01-2020,,,
# Created by: user9284,,,
# Compay XYZ,,,
# ,,,
# Data,Country,Units,Revenue
# 2019-01-08,USA,343,15461.36
# 2019-01-04,Panama,343,4681.36
# 2019-01-07,Panama,93,2220.36
# 2019-01-16,Brazil,42,2220.36
# 2019-01-07,USA,103,1853.36
# 2019-01-24,Canada,28,286.36
# 2019-01-26,Canada,323,1593.36
# 2019-01-28,Canada,63,3228.36
# 2019-01-13,Canada,264,257.36
# 2019-01-28,Brazil,27,3026.36

import csv

employees = [["Name", "Age", "Job"],
            ["Spongebob", 30, "Cook"],
            ["Patick", 36, "Unemployed"],
            ["Sandy", 27, "Scientist"]]

file_path = "C:/Users/LAPTOP GADGET/Desktop/test/output.csv"

try:
    with open(file=file_path, mode="w", newline="") as file:
        write = csv.writer(file)
        for row in employees:
            write.writerow(row)
        print(f"csv file '{file_path}' was created")
except FileExistsError:
    print(f"That file already exists!")
except TypeError:
    print()