# docs.python.org/3/library/functions.html#map
# map(function, iterable, ...)
# list comprehensions

print()

# def main():
#     # yell("This is CS50")
#     yell(["This", "is", "CS50"])
#
# # def yell(phrase):
# #     print(phrase.upper())
#
# def yell(words):
#     uppercase = []
#     for _ in words:
#         uppercase.append(_.upper())
#     print(*uppercase)

def main():
    yell("This", "is", "CS50")

# def yell(*words):
#     uppercase = map(str.upper, words)
#     print(*uppercase)

def yell(*words):
    uppercase = [word.upper() for word in words]
    print(*uppercase)

if __name__ == "__main__":
    main()

