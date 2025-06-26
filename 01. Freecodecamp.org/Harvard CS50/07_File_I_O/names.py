print()

names = []
for _ in range(3):
    names.append(input("What's your name? "))

print()
for name in sorted(names):
    print(f"Hello, {name}")

