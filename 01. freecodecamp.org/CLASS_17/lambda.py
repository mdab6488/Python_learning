from functools import reduce


# lambda num : num * num
def squared(num):
    return num * num


print(squared(2))


# lambda addTwo : a + 2
def addTwo(num):
    return num + 2


print(addTwo(5))


# lambda a, b : a + b
def sum_total(a, b):
    return a + b


print(sum_total(2, 3))


#######################################################
def funcBuilder(x):
    return lambda num: num + x


addTen = funcBuilder(10)
addTwenty = funcBuilder(20)

print(addTen(7))
print(addTwenty(7))

#######################################################
numbers = [3, 7, 12, 18, 20, 21, 25, 30]

squared_nums = map(lambda num: num * num, numbers)

print(list(squared_nums))

#######################################################
odd_nums = filter(lambda num: num % 2 != 0, numbers)
print(list(odd_nums))

#######################################################
numbers = [1, 2, 3, 4, 5, 1]
total = reduce(lambda acc, curr: acc + curr, numbers)

print(total)

total = reduce(lambda acc, curr: acc + curr, numbers, 100)
print(total)

name = ["Dave Gray", "Sara Ito", "John jacob Jingleheimerschmidt"]
char_count = reduce(lambda acc, curr: acc + len(curr), name, 0)
print(char_count)
#######################################################

print(sum(numbers))
print(sum(numbers, 200))
