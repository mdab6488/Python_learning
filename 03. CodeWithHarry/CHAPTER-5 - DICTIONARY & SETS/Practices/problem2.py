s = set()

print()
for n in range(8):
    number = n + 1
    num = int(input(f"Enter number {number}: "))
    s.add(num)

print(s)
print(f"Length: {len(s)}")