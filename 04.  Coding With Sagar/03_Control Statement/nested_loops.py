print()
for i in enumerate(range(1,3), start=1):
    print(f"{i[0]}. loop: {i[1]}")
    for j in enumerate(range(3, 6), start=1):
        print(f"- {j[0]}. Second loop: {j[1]}")
    print()

"""
1. loop: 1
- 1. Second loop: 3
- 2. Second loop: 4
- 3. Second loop: 5

2. loop: 2
- 1. Second loop: 3
- 2. Second loop: 4
- 3. Second loop: 5
"""


