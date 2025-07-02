print()

i = 1
while i <= 5: # False
    print(i, end=", ")
    i += 1

print()
numbers = [1,2,3,4,5]
for number in numbers:
    print(number, end=", ")

print()
# range(start, stop, step)
for i in range(1, 10, 2):
    print(i, end=", ")

print()
for num in range(1, 10, 1):
    if num == 5:
        break
    print(num, end="")

print()
for num in range(1,5):
    if num == 3:
        continue # Skip
    print(num, end="")

print()
for lazy in range(20):
    pass

"""
1-10
even numbers
2,4,6,8,10
Odd numbers
1,3,5,7,9

%2 == 0
2 % 4 = 0
"""
print()
for even in range(1, 11):
    if even % 2 == 0:
        print(even, end=", ")

print()
for odd in range(1, 11):
    if odd % 2 != 0:
        print(odd, end=", ")

print()
print()
start = int(input("Enter start = "))
stop = int(input("Enter stop = "))
skip = int(input("Enter skip = "))

for i in range(start, stop):
    if start <= skip <= stop:
        if i == skip:
            continue
    else:
        print("Invalid Number")
        break
    print(i, end=", ")

