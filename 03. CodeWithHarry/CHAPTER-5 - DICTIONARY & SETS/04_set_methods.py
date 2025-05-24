s = {1, 5, 32, 54, 5, 5, 5, "Harry"}

print()
print(type(s)) #<class 'set'>
print(s)
print()

s.add(566)
print(s)
print(len(s))
print()
s.remove(54)
print(s)
print(len(s))
print()
s.pop()
print(s)