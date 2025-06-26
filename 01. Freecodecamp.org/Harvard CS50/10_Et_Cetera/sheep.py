# docs.python.org/3/howto/functional.html#generators
# generators
# yield
# iterators

print()

# def main():
#     number_of_sheep = int(input("What's n? "))
#     for s in sheep(number_of_sheep):
#         print(s)
#
# def sheep(n):
#     flock = []
#     for i in range(n):
#         flock.append("🐏" * i)
#     return flock

def main():
    number_of_sheep = int(input("What's n? "))
    for s in sheep(number_of_sheep):
        print(s)

def sheep(n):
    for i in range(n):
        yield "🐏" * i

if __name__ == "__main__":
    main()