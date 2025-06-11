# function = A block of reuseable code
#            place() after the function name to invoke it
print(f"{"*" * 20}")
print(f"{" " * 5} FUNCTIONS {" " * 5}")
print(f"{"*" * 20}")
def happy_birthday(name, age):
    print(f"Happy birthday to {name}")
    print(f"You are {age} years old!")
    print("Happy birthday to you!")
    print()

happy_birthday("MD ABDUR RAHMAN", 27)
happy_birthday("Riyan", 23)

def display_invoice(username, amount, due_date):
    print(f"Hello {username}")
    print(f"Your bill of ${amount:.2f} is due: {due_date}")

display_invoice("mdab6488", 42.50, "01/01/2026")

print(f"{"*" * 20}")
print(f"{" " * 5} RETURN {" " * 5}")
print(f"{"*" * 20}")

# return = statement used to end a function
#          and send a result back to the caller

def add(x, y):
    z = x + y
    return z

def subtract(x, y):
    z = x - y
    return z

def multiply(x, y):
    z = x * y
    return z

def divide(x, y):
    z = x / y
    return z

print(add(10, 15))
print(subtract(20, 17))
print(multiply(50, 3))
print(divide(60, 20))
print()

def create_name(first, last):
    first = first.upper()
    last = last.upper()
    return f"{first} {last}"

full_name = create_name("md abdur", "rahman")
full_name2 = create_name("Riyan", "Kabir")
print(full_name)
print("🥰😍")
print(full_name2)