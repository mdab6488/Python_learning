print()

"""
[expression for item in iterable if condition]

e - x * 2
item - 
iterable - range(1, 11)
condition optional
"""

"""
squares = []
for i in range(1, 11):
    squares.append(i ** 2)
print(squares) # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
"""
seqares_1 = [i ** 2 for i in range(1, 11)]
print(seqares_1) # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

seqares_2 = [i ** 2 for i in range(1, 11) if i % 2 == 0]
print(seqares_2) # [4, 16, 36, 64, 100]



