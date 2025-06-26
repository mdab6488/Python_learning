print()
def f(*args, **kwargs):
    # print(f"Positional: {args}")
    print(f"Name: {kwargs}")

# f(100, 50, 25, 5) # Positional: (100, 50, 25, 5)
f(galleons=100, sickles=50, knuts=25)
# Name: {'galleons': 100, 'sickles': 50, 'knuts': 25}

# def my_print(*objects, sep="", end="\n"):
#     for object in objects:
#         ...

