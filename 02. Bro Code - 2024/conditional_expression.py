# conditional expression = A one-line shortcut for the if-else statement (ternary operator)
#                          Print or assign one of two values base on condition
#                          X if condition else Y

num = 5
a = 6
b = 7
age = 13
temprature = 30
user_role = "guest"

# print("Positive" if num > 0 else "Negative")
# result = "Even" if num % 2 == 0 else "ODD"
# print(result)

# max_num = a if a > b else b
# min_num = a if a < b else b
# print(f"Max Number: {max_num}")
# print(f"Min Number: {min_num}")

# status = "Adult" if age >= 18 else "Child"
# print(status)

# weather = "HOT" if temprature > 20 else "COLD"
# print(weather)

access_lavel = "Full Access" if user_role == "admin" else "Limited Acess"
print(access_lavel)