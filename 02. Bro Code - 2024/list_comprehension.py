# list comprehension = A concise way to create lists in Python
#                      Compact and easier to read that traditional loops
#                      [expression for value in iterable if condition]

# doubles = []
# for x in range(1, 11):
#     doubles.append(x)
#
# print(doubles)

# doubles = [x * 2 for x in range(1, 11)]
# triples = [y * 3 for y in range(1, 11)]
# squares = [z * z for z in range(1, 11)]
#
# print(doubles)
# print(triples)
# print(squares)

# fruits = ["apple", "orange", "banana", "coconut"]
# fruits = [fruit.upper() for fruit in fruits]
#
# print(fruits)

# fruits = ["apple", "orange", "banana", "coconut"]
# fruit_chars = [fruit[0] for fruit in fruits]
#
# print(fruit_chars)

numbers = [1, -2, 3, -4, 5, -6, 8, -9]
positive_nums = [num for num in numbers if num >= 0]
negative_nums = [num for num in numbers if num < 0]
even_nums = [num for num in numbers if num % 2 == 0]
odd_nums = [num for num in numbers if num % 2 == 1]

print(f"Positive Numbers: {positive_nums}")
print(f"Negative Numbers: {negative_nums}")
print(f"Even Numbers: {even_nums}")
print(f"Odd Numbers: {odd_nums}")

print("")

grades = [85, 42, 79, 90, 56, 61, 30]
passing_grades = [grade for grade in grades if grade >= 60]
print(f"Passing Grades: {passing_grades}")
