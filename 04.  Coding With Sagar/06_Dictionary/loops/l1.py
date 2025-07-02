print()

profile = {
    "name": "MD ABDUR RAHMAN", "age": 28, "salary": 10000000
}
# name
# age
# salary
for key in profile:
    print(key)

print()
# MD ABDUR RAHMAN
# 28
# 10000000
for key in profile.values():
    print(key)

print()
# ('name', 'MD ABDUR RAHMAN')
# ('age', 28)
# ('salary', 10000000)
for key in profile.items():
    print(key)