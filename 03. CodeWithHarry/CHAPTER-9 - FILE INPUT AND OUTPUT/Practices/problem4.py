
print()
word = "Riyan"

with open("file.txt", "r") as f:
    content = f.read()

contentNew = content.replace(word, "Riyan Kabir")

with open("file.txt", "w") as f:
    f.write(contentNew)