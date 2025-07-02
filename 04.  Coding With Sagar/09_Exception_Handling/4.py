
print()
# check password strength
def check_password(pas):
    if len(pas) < 8:
        raise Exception("Error: Password must be >= 8 character")
    print("Passowrd is strong")

try:
    password = input("Enter a password = ")
    check_password(password)
except Exception as e:
    print(e)