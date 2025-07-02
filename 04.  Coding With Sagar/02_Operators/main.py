print()

# 🧠 Python Operator Precedence (PEMDAS / BODMAS)
"""
| Description                                        | Operators           | Example             |
| -------------------------------------------------- | ------------------- | ------------------- |
| **P** – Parentheses                                | `()`                | `(2 + 3) * 4 = 20`  |
| **E** – Exponentiation                             | `**`                | `2 ** 3 = 8`        |
| **MD** – Multiplication & Division (left to right) | `*`, `/`, `//`, `%` | `10 / 2 * 3 = 15.0` |
| **AS** – Addition & Subtraction (left to right)    | `+`, `-`            | `5 + 2 - 1 = 6`     |

result = 3 + 2 * (4 ** 2) // 8 - 1
result = 3 + 2 * 16 // 8 - 1
result = 3 + 32 // 8 - 1
result = 3 + 4 - 1

# Step-by-step:
# 4 ** 2 = 16
# 2 * 16 = 32
# 32 // 8 = 4
# 3 + 4 - 1 = 6
print(result)  # Output: 6
"""

result = 10 + 5 * 2
print(result)