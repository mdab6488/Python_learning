# fruits =        ["apple", "orange", "banana", "coconut"]
# vegetables =    ["celery", "carrots", "potatoes"]
# meats =         ["chicken", "fish", "turkey"]

# fruits =        ("apple", "orange", "banana", "coconut")
# vegetables =    ("celery", "carrots", "potatoes")
# meats =         ("chicken", "fish", "turkey")

fruits =        {"apple", "orange", "banana", "coconut"}
vegetables =    {"celery", "carrots", "potatoes"}
meats =         {"chicken", "fish", "turkey"}

groceries = [fruits, vegetables, meats]

# fruits[0] = "pineapple"
# print(groceries)
# print(groceries[0][0].capitalize())

for collection in groceries:
    print(collection)
    for food in collection:
        print(food, end=" ")
    print()