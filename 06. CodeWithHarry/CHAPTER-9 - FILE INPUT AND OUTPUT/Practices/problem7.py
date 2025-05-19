
print()

with open("log.txt", "r") as f:
    lines = f.readlines()

lineNumber = 1
word = "Python"
for line in lines:
    if word in line:
        print(f"Yes, '{word}' is present. Line no: {lineNumber}")
        break
    lineNumber += 1
else:
    print(f"No, '{word}' is not present")