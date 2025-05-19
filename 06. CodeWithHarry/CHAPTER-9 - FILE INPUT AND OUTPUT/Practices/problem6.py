
print()
with open("log.txt", "r") as f:
    content = f.read()

word = "python"
if word in content:
    print(f"Yes, '{word}' is present")
else:
    print(f"No, '{word}' is not present")