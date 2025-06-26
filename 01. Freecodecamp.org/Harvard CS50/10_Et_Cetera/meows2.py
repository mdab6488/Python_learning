# pip install mypy
# mypy.readthiedocs.io
# peps.python.org/pep-0257

# def meow(n: int) -> None:
#     for _ in range(n):
#         print(f"meow {_ + 1}")
#
# print()
# # number: int = int(input("Number: "))
# # meow(number)
#
# number: int = int(input("Number: "))
# meows: str = meow(number)
# print(meows)
# # print(type(number)) # <class 'int'>
# # print(type(meows)) # <class 'NoneType'>

def meow(n: int) -> str:
    """
    Meow n times

    :param n: Number of times to meow
    :type n: int
    :raise TypeError: if n is not an int
    :return: A stirng of n meows, on per line
    :rtype: str
    """
    return f"meow\n" * n

print()
number: int = int(input("Number: "))
meows: str = meow(number)
print(meows, end="")
# print(type(number)) # <class 'int'>
# print(type(meows)) # <class 'str'>
