print()

profile = {
    "name": "MD ABDUR RAHMAN", "age": 28, "salary": 10000000
}

print(profile) # {'name': 'MD ABDUR RAHMAN', 'age': 28, 'salary': 10000000}
pop_item = profile.popitem()
print(pop_item) # ('salary', 10000000)
print(profile) # {'name': 'MD ABDUR RAHMAN', 'age': 28}