name = "MD ABDUR RAHMAN"
count = 1


def another():
    color = "blue"
    # count = 2
    # count += 1
    global count
    count += 1

    print(count)

    def greeting(name):
        nonlocal color
        color = "red"
        print(f"Hello, {color}")
        print(f"Hello, {name}")

    greeting("Rahman")


another()
