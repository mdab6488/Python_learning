# name = input("Enter your full name: ")

# result = len(name)
# result = name.find("R") # Case Sensitive
# result = name.rfind("R") # Case Sensitive

# name = name.capitalize()
# name = name.upper()
# name = name.lower()

# result = name.isdigit()
# result = name.isalpha()
#
# print(result)

# phone_number = input("Enter your phone #: ")
#
# # result = phone_number.count("-")
# phone_number = phone_number.replace("-", "")
#
# print(phone_number)

username = input("Enter you username: ")

if len(username) > 12:
    print("Your username can't be more then 12 characters")
elif not username.find(" ") == -1:
    print("Your username can't contain spaces")
elif not username.isalpha():
    print("Your username can't contain number")
else:
    print(f"Welcome {username}")

result = username.isalpha()
print(result)

# print(help(str))