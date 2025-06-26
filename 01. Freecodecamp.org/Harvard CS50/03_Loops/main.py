print()
# print("meow\n" * 3, end="")

def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("What's x? "))
        if n > 0:
            break
    return n

def meow(number_of_times):
    for _ in range(number_of_times):
        print("meow")

main()