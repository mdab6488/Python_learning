infos = {"name": "Riyan", "age": 20, "isStudent": True, "color": "White"}

# print(infos["name"])

# infos["name"] = "Alamin"
# print(infos)

# print(infos.get("color", "Blue"))

# print(infos.pop("color"))
# print(infos)

# print(infos.popitem())
# print(infos)

# print("color" in infos)
print(len(infos))

# print(infos.keys())
# print(list(infos.keys()))
# print(infos.values())
# print(list(infos.values()))

# print(list(infos.items()))

infos["favorite food"] = "Kacchi Biryani"
print(infos)

del infos["color"]

infosCopy = infos.copy()
print(infosCopy)
