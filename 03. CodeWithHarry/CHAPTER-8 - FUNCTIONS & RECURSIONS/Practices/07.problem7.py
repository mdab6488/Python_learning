print()

def rem(letter, word):
    n = []
    for item in letter:
        if not item == word:
            n.append(item.strip(word))
    return n
        # letter.remove(word)
        # return letter
    # return None

l = ["Riyan", "Alamin", "Riyan asdfg", "MD AB asdfg", "asdfg"]

print(rem(letter=l, word="asdfg"))
