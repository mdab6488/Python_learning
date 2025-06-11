
print()
with open("poem.txt") as f:
    content = f.read()
    word = "Riyan"
    if word in content:
        print(f"The word '{word}' is present in the content")
    else:
        print(f"The word '{word}' is not present in the content")


