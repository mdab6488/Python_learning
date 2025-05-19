
print()
words = ["Riyan Kabir", "good", "Dear"]

with open("file2.txt", "r") as f:
    content = f.read()

for word in words:
    content = content.replace(word, "#" * len(word))

with open("file2.txt", "w") as f:
    f.write(content)