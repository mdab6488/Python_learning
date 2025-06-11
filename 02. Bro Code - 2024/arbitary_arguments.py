# *args = allows you to pass multiple non-key arguments
# **kwargs = allows you to pass multiple keyword-arguments
#            * unpacking operator
#            1. positional 2. default 3. keyword 4. ARBITRARY

# def add(a, b):
#     return a + b
#
# print(add(1, 2))

print(f"{"*" * 24}")
print(f"{" " * 8} *args {" " * 8}")
print(f"{"*" * 24}")

def add(*args):
    # print(type(args)) #<class 'tuple'>
    total = 0
    for arg in args:
        total += arg
    return total

print(add(1, 2, 3, 4, 5))

def add(*nums):
    # print(type(nums))
    total = 0
    for num in nums:
        total += num
    return total

print(add(1, 2, 3, 4, 5))

def display_name(*args):
    for arg in args:
        print(arg, end=" ")

display_name("Mr.", "Riyan", "Kabir")

print(f"\n{"*" * 24}")
print(f"{" " * 8} **kwargs {" " * 8}")
print(f"{"*" * 24}")

def print_address(**kwargs):
    # print(type(kwargs)) #<class 'dict'>
    # for key in kwargs.keys():
    #    print(key)
    for key, value in kwargs.items():
        print(f"{key.capitalize():10}: {value}")

print_address(street="123 Fake St. ",
              apt="100",
              city="Detroit",
              state="MI",
              zip="54321")

print(f"{"*" * 24}")
print(f"{" " * 3} *args & **kwargs {" " * 3}")
print(f"{"*" * 24}")
def shipping_lable(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print("\n")
    for key, value in kwargs.items():
        print(f"{key}: {value}")
    print("\n")

    if "apt" in kwargs:
        print(f"{kwargs.get('street')} {kwargs.get('apt')}")
    elif "pobox" in kwargs:
        print(f"{kwargs.get('street')} {kwargs.get('pobox')}")
    else:
        print(f"{kwargs.get('street')}")

    print(f"{kwargs.get('city')} {kwargs.get('state')} {kwargs.get('zip')}")

shipping_lable("Dr.", "Spongebob", "Squarepants", "III",
               street="123 Fake St.",
               pobox="PO box #1001",
               # apt="#100",
               city="Detroit",
               state="MI",
               zip="54321")