
print()
n = int(input("Enter a number: "))
i = 1
s = 0
while i<=n:
    print(f"s: {s} + i: {i} = {s + i}")
    s += i
    i += 1

print("*" * 30)
print(f"Total: {s}")
print("*" * 30)