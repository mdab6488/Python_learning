
print()
for i in range(10):
    print(i, end=" ")

print()
for i in range(10):
    if i == 8:
        break # Exit the loop right now.
    print(i, end=" ")

print()
for i in range(10):
    if i == 8:
        continue # Skip this iteration.
    print(i, end=" ")

print()