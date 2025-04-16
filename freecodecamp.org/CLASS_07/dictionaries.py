# Dictionaries

band = {
    "vocals": "plant",
    "guitar": "page",
    "bass": "jones",
}

band2 = dict(vocals="Plant", guitar="Page", bass="Jones")

print(band)
print(band2)

print("-------------------")

print(type(band))
print(len(band2))

# Acess items
print("\n Acess items")
print(band["vocals"])
print(band.get("guitar"))

# list all keys
print("\n list all keys")
print(band.keys())

# list all values
print("\n list all values")
print(band.values())


# list of key/values pairs as tuples
print("\n list of key/values pairs as tuples")
print(band.items())

# Verify a key exists
print("\n Verify a key exists")
print("vocals" in band)
print("drums" in band)

# Change values
print("\n Change values")
band["vocals"] = "Robert Plant"
# band.update({"guitar": "Jimmy Page"})
band["guitar"] = "Jimmy Page"
print(band)

# Remove items
print("\n Remove items")
print(band.pop("bass"))
print(band)

band["drums"] = "Bonham"
print(band)

print(band.popitem())  # tuple
print(band)

# Delete and Clear
print("\n Delete and Clear")
band["drums"] = "Bonham"
del band["drums"]
print(band)

band2.clear()
print(band2)

del band2

# Copy dictionaries
# print("\n Copy dictionaries")
# band2 = band  # Creates a reference to the original dictionary
# print("Bad copy!")
# print(band2)
# print(band)

# band2["drums"] = "Bonham"
# print(band)

band2 = band.copy()  # Creates a shallow copy of the original dictionary
band2["drums"] = "Bonham"
print("Good copy!")
print(band)
print(band2)

# or user the dict() constructor function
print("\n or user the dict() constructor function")
band3 = dict(band)  # Creates a shallow copy of the original dictionary
print("Good copy!")
print(band3)

# Nested dictionaries
print("\n Nested dictionaries")
member1 = {
    "name": "Plant",
    "instrument": "vocals",
}
member2 = {
    "name": "Page",
    "instrument": "guitar",
}
member2 = {
    "name": "Robert Plant",
    "instrument": "vocals",
    "age": 75,
}
band = {
    "member1": member1,
    "member2": member2,
}
print(band)
print(band["member1"]["name"])

# Sets
print("\n Sets")
nums = {1, 2, 3, 4}

nums2 = set([1, 2, 3, 4])
print(nums)
print(nums2)
print(type(nums))
print(len(nums))

# No duplicates allowed
print("\n No duplicates allowed")
nums = {1, 2, 3, 4, 3, 2}
print(nums)

# True is a dupe of 1, flase is a dupe of 0
print("\n True is a dupe of 1, flase is a dupe of 0")
nums = {1, True, 2, False, 3, 4, 0}
print(nums)

# Check if a value is in a set
print("\n Check if a value is in a set")
print(1 in nums)

# But you cannot refer to an element in the set with an index position or key

# Add a new element to a set
nums.add(8)
print(nums)

# Add elements from one set to another
morenums = {5, 6, 7}
nums.update(morenums)
print(nums)

# you can use update with lists, tuples, and dictonaries, too.

# Marge two sets to create a new sets
one = {1, 2, 3}
two = {4, 5, 6}

mynewset = one.union(two)
print(mynewset)

# Keep only the duplicates
print("\n Keep only the duplicates")
one = {1, 2, 3}
two = {2, 3, 1, 4, 5}

one.intersection_update(two)  # Keep only the duplicates in one
print(one)

# Keep everything that is not a duplicate
print("\n Keep only the duplicates")
one = {1, 2, 3}
two = {2, 3, 4, 5}

one.symmetric_difference_update(two)  # Keep everything that is not a duplicate in one
print(one)
