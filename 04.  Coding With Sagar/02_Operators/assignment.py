print()
# for assign values
"""
| Operator | Name                    | Example   | Same As      | Result in `x` |
| -------- | ----------------------- | --------- | ------------ | ------------- |
| `=`      | Assignment              | `x = 5`   | —            | `5`           |
| `+=`     | Add and assign          | `x += 3`  | `x = x + 3`  | `8`           |
| `-=`     | Subtract and assign     | `x -= 2`  | `x = x - 2`  | `6`           |
| `*=`     | Multiply and assign     | `x *= 4`  | `x = x * 4`  | `24`          |
| `/=`     | Divide and assign       | `x /= 3`  | `x = x / 3`  | `8.0`         |
| `//=`    | Floor divide and assign | `x //= 2` | `x = x // 2` | `4`           |
| `%=`     | Modulus and assign      | `x %= 5`  | `x = x % 5`  | `4`           |
| `**=`    | Power and assign        | `x **= 2` | `x = x ** 2` | `16`          |
"""

x = 5
x += 2      # x = 7
x *= 3      # x = 21
x //= 4     # x = 5
print(x)    # Output: 5
