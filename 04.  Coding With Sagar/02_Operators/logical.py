print()
# for combine
"""
| Operator | Name | Meaning                               | Example         | Result  |
| -------- | ---- | ------------------------------------- | --------------- | ------- |
| `and`    | AND  | True **only if both** sides are True  | `True and True` | `True`  |
| `or`     | OR   | True if **at least one** side is True | `True or False` | `True`  |
| `not`    | NOT  | Flips True to False and False to True | `not True`      | `False` |

and: “Both must be True!”
✅✅ → ✅
✅❌ → ❌
❌❌ → ❌

or: “At least one must be True!”
✅❌ → ✅
❌❌ → ❌
✅✅ → ✅

not: “Flip it!”
not True → False
not False → True
"""

x = 5
y = 10

print(x > 0 and y > 0)    # True, because both are greater than 0
print(x > 10 or y > 5)    # True, because y > 5
print(not x > 10)         # True, because x > 10 is False → not False = True

age = 20
is_student = True
print(age > 18 and is_student) # True
print(age > 28 or is_student) # True
print(not is_student) # False
