print()

my_dict = {
    "name": "python", "version": 3.9, "Use_Case": ["AI", "ML", "DS", "WD"]
}

print(my_dict) # {'name': 'python', 'version': 3.9, 'Use_Case': ['AI', 'ML', 'DS', 'WD']}
del my_dict["version"]
print(my_dict) # {'name': 'python', 'Use_Case': ['AI', 'ML', 'DS', 'WD']}