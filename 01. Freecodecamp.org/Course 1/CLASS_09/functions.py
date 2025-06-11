# def hello_world():
#     print("Hello World")


# hello_world()


# def sum(num1, num2):
#     print(num1 + num2)


# sum(5, 10)
# sum(1, 7)
# sum(2, 3)


# def sum(num1=0, num2=0):
#     return 0 if type(num1) is not int or type(num2) is not int else num1 + num2


# total = sum()
# print(total)

# def sum(num1=0, num2=0):
#     if type(num1) is not int or type(num2) is not int:
#         return 0
#     return num1 + num2


# total = sum()
# print(total)


def multiple_items(*args):
    print(args)
    print(type(args))


multiple_items("Dave", "John", "Mary")


def mult_name_items(**kwargs):
    print(kwargs)
    print(type(kwargs))


mult_name_items(
    first="Dave",
    last="Smith",
)
