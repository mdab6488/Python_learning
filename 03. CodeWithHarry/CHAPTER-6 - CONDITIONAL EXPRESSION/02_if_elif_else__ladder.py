print()
a = int(input("Enter you age: "))

# If elif else statement

if 100 > a >= 18:
    print("👍 You are above the age of consent")
    print("Good for you")
elif a < 0:
    print("❌ You are entering an invalid age")
elif a >= 100:
    print("🧓 You are too old for age of consent")
else:
    print("👶 You are below the age of consent")

print()
print("*" * 30)
print("End of Program")
print("*" * 30)