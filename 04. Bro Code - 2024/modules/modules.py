# module = a file containing code you want to include in your program
#          use 'import' to a module (built-in or your own)
#          useful to break up a large program-reuseable separate files
import math
import example

# import math as m
# from math import pi, e

# print(help("modules"))
# print(help("math"))

a, b, c, d, e = 1, 2, 3, 4, 5
print(math.e ** a)
print(math.e ** b)
print(math.e ** c)
print(math.e ** d)
print(math.e ** e)

print()

# print(math.pi)
# print(m.pi)
print(math.pi)
print(math.e)

print()

# result = example.pi
# result = example.square(3)
# result = example.cube(3)
# result = example.circumference(3)
result = example.area(3)
print(result)