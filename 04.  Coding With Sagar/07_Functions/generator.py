print()

# yield keyword
def count_down(num):
    while num > 0:
        yield num # yeild valu one at a time
        num -= 1

# using the generator
for number in count_down(5):
    print(number)

