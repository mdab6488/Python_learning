from functools import reduce

# Map Example
l = [1, 2, 3, 4, 5]

square = lambda x: x * x
sqlist = map(square, l)

print()
print(list(sqlist))

# Filter Example
def even(n):
    if n%2 == 0:
        return True
    return False

onlyEven = filter(even, l)

print(list(onlyEven))

# Reduce Example
sum_def = lambda a,b: a + b
mul = lambda x, y: x * y

print(reduce(sum_def, l)) # 15
# 1, 2, 3, 4, 5
# 3, 3, 4, 5
# 6, 4, 5
# 10, 5
# 15

print(reduce(mul, l)) # 120
# 1, 2, 3, 4, 5
# 2, 3, 4, 5
# 6, 4, 5
# 24, 5
# 120