# docs.python.org/3/library/functions.html#print
# docs.python.org/3/library/stdtypes.html#string-methods

# python hello.py
# Ask user for their name
print()
name = input("What's you name? ").strip().title()

# Remove whitespace from str
# name = name.strip()

# Capitalize user's name
# name = name.capitalize()
# name = name.title()

"""
Split user's name into first name and last name
"""
first, last = name.split(" ")

"""
Say hello to user
"""
# print("hello,")
# print(name)
# print("Hello,", name)
# print("Hello, " + name)

# print(*objects, sep=' ', end="\n", file=sys.stdout, flush=False)

# print("hello, ", end="")
# print(name)

# print("hello,", name, sep="???")

# print('hello, "friend"')
# print("hello, 'friend'")
# print("hello, \"friend\"")

print(f"hello, {first}")

# =====================
# Argument
# =====================
# An argument is the input you give to a function to change how it works. For example, in Python, the print() function takes a string (text) as its argument. So when you write:
# print("Hello, world")
# You’re telling Python to show “Hello, world” on the screen. This is called a side effect—something the program does, like showing text or sound. In this case, the side effect is showing a message on the screen. That’s what your first program does!

