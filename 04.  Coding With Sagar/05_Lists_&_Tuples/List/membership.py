print()

"""
in - True/False
not in - opposit
"""

my_list = [1, 2, 4, 5, 6, 7, 9]
check = int(input("Enter a number to check: "))
if check in my_list:
    print("Your number is available in the list")

if check not in my_list:
    print("Your number is not available in the list")