p1 = "Make a lot of money"
p2 = "buy now"
p3 = "subscribe this"
p4 = "click this"

print()
massage = input("Enter your comment: ")

if (p1 in massage) or (p2 in massage) or (p3 in massage) or (p4 in massage):
    print("❌ This comment is a spam")
else:
    print("✔️ This comment is not a spam")

