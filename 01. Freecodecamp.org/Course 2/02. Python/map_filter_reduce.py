# map(), filter(), reduce()


# numbers = [1, 2, 3, 4, 5]


# def double(a):
#     return a * 2

# double = lambda a: a * 2

# result = map(lambda a: a * 2, numbers)
# print(result)  # <map object at 0x7f8c4c2a3d90>
# print(list(result))  # [2, 4, 6, 8, 10]


# def isEven(n):
#     return n % 2 == 0


# result = filter(lambda n: n % 2 == 0, numbers)
# print(list(result))  # [2, 4]

from functools import reduce

expenses = [("Dinner", 80), ("Car repair", 120)]

sum = reduce(lambda a, b: a[1] + b[1], expenses)

# for expense in expenses:
#     sum += expense[1]


print(sum)  # 200
