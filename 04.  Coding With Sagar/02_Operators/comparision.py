print()
# for comare values
"""
| Operator | Name                     | Meaning                        | Example  | Result |
| -------- | ------------------------ | ------------------------------ | -------- | ------ |
| `==`     | Equal to                 | Is it the same?                | `5 == 5` | `True` |
| `!=`     | Not equal to             | Is it different?               | `5 != 3` | `True` |
| `>`      | Greater than             | Is it bigger?                  | `7 > 4`  | `True` |
| `<`      | Less than                | Is it smaller?                 | `3 < 8`  | `True` |
| `>=`     | Greater than or equal to | Is it bigger **or** the same?  | `5 >= 5` | `True` |
| `<=`     | Less than or equal to    | Is it smaller **or** the same? | `2 <= 3` | `True` |
"""

a = 6
b = 4

print(f"{a} is Equal to {b}: {a == b}")   # 6 is Equal to 4: False
print(f"{a} is Not equal to {b}: {a != b}")   # 6 is Not equal to 4: True
print(f"{a} is Greater than {b}: {a > b}")   # 6 is Greater than 4: True
print(f"{a} is Less than {b}: {a < b}")   # 6 is Less than 4: False
print(f"{a} is Greater than or equal to {b}: {a >= b}")   # 6 is Greater than or equal to 4: True
print(f"{a} is Less than or equal to {b}: {a <= b}")   # 6 is Less than or equal to 4: False

x = 5
y = 5
print(f"{a} is Not equal to {b}: {x != y}")   # 6 is Not equal to 4: False
