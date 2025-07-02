print()

profile = {
    "name": "MD ABDUR RAHMAN", "age": 28, "salary": 10000000
}

# dict.get()
age = profile.get("age", "Not Found")
age_2 = profile.get("age_2", "Not Found")
print(age, age_2)

