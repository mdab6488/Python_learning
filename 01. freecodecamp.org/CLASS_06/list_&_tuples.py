users = ["Dave", "John", "Mary", "Anna", "Tom"]

data = ["Dave2", 42, True]

emptylist = []

print("Dave" in emptylist)

print(users[0])
print(users[-1])
print(users[-2])

print(users.index("Mary"))

# print(users[0:2])
print(users[:2])
print(users[1:])
print(users[-3:-1])

print(len(data))

users.append("Alamin")
print(users)

users += ["AB"]
print(users)

users.extend(["Robert", "Martha"])
print(users)

# users.extend(data)
# print(users)

users.insert(0, "Riyan")
print(users)

users[2:2] = ["Rita", "Sita"]
print(users)

users[1:3] = ["Rita 1", "Sita 1"]
print(users)

users.remove("Rita 1")
print(users)

print(users.pop())

del users[1]
print(users)

# del data
data.clear()
print(data)

users[1:2] = ["dave"]
users.sort()
print(users)

users.sort(key=str.lower)
print(users)

nums = [4, 42, 78, 1, 5]
nums.reverse()
print(nums)

# nums.sort(reverse=True)
# print(nums)

print(sorted(nums, reverse=True))
print(nums)

numscopy = nums.copy()
mynums = list(nums)
mycopy = nums[:]
# print(numscopy)
# print(mynums)
# print(mycopy)
# print(nums)

print("")

print(numscopy)
print(mynums)
mycopy.sort()
print(mycopy)
print(nums)

print(type(nums))

# mylist = list([1, "Neil", True])

mylist = [1, "Neil", True]
print(mylist)

print("")

# Tuples
# mytuple = tuple(('Dave', 42, True))
mytuple = ("Dave", 42, True)

anothertuple = (1, 4, 2, 8, 2, 2)

print(mytuple)
print(type(mytuple))
print(type(anothertuple))

newlist = list(mytuple)
newlist.append("Alamin")
newtuple = tuple(newlist)
print(newtuple)

# (one, two, *hey) = anothertuple
(one, *two, hey) = anothertuple
print(one)
print(two)
print(hey)

print(anothertuple.count(2))
