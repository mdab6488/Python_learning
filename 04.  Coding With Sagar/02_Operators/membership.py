print()

"""
| Operator | Name   | Meaning                                | Example              | Result |
| -------- | ------ | -------------------------------------- | -------------------- | ------ |
| `in`     | In     | True if value **exists** in collection | `'a' in 'apple'`     | `True` |
| `not in` | Not In | True if value **does NOT exist**       | `3 not in [1, 2, 4]` | `True` |
"""
# for valu exist in sequences
# 🔤 Strings:
print('a' in 'banana')       # True
print('z' not in 'pizza')    # False

# 📦 Lists:
fruits = ['apple', 'banana', 'mango']
print('banana' in fruits)     # True
print('grape' not in fruits)  # True

# 🧩 Dictionary (checks keys, not values!):
info = {'name': 'Abdur Rahman', 'age': 22}
print('name' in info)         # True (key check)
print('Abdur' in info)        # False (value not checked)
