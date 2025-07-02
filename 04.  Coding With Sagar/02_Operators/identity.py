print()
# for object memory location
"""
| Operator | Name   | Meaning                                             | Example      | Result            |
| -------- | ------ | --------------------------------------------------- | ------------ | ----------------- |
| `is`     | Is     | True if both variables refer to the **same object** | `a is b`     | `True` or `False` |
| `is not` | Is Not | True if they **do not** refer to the same object    | `a is not b` | `True` or `False` |
"""

a = [1, 2, 3]
b = a           # b points to the same list
c = [1, 2, 3]   # c is a different list with the same values

print(a is b)       # True (same object)
print(a is c)       # False (same value, different object)
print(a == c)       # True (values are equal)
print(a is not c)   # True (different objects)
