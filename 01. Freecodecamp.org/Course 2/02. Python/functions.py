# def hello(name="Unknown", age=0):
#     print(f"Hello, {name} you are {age} years old!")


# hello("Riyan", 23)
# hello("Alamin", 27)
# hello()


# def change(value):
#     # value = 10  # This will not change the original value outside the function
#     value["name"] = "Alamin"  # This will change the original value outside the function
#     value["age"] = 27  # This will change the original value outside the function


# # val = 5
# val = {"name": "Riyan", "age": 23}
# change(val)

# print(val)


# def hello(name):
#     print(f"Hello, {name}!")
#     return name


# hello("Riyan")


# def hello(name):
#     if not name:
#         return
#     print(f"Hello, {name}!")


# hello(False)
# hello("Riyan")


# def hello(name):
#     print(f"Hello, {name}!")
#     return name, "Alamin", 27


# print(hello("Riyan"))

# ============================================
# Variable Scope
# ============================================
# age = 23  # Global variable


# def test():
#     age = 27  # Local variable
#     print(age)  # Accessing global variable


# print(age)  # Accessing global variable
# test()  # Accessing local variable


# ============================================
# Nested Functions
# ============================================
# def talk(phrase):
#     def say(word):
#         print(f"{word}")

#     words = phrase.split(" ")
#     for word in words:
#         say(word)


# talk("Hello, how are you?")


# def count():
#     count = 0

#     def increment():
#         nonlocal count  # Use the nonlocal keyword to modify the outer variable
#         count += 1
#         print(count)

#     increment()


# count()


# ============================================
# Closures Functions
# ============================================
def counter():
    count = 0

    def increment():
        nonlocal count  # Use the nonlocal keyword to modify the outer variable
        count += 1
        return count

    return increment


increment = counter()

print(increment())  # Output: 1
print(increment())  # Output: 2
print(increment())  # Output: 3
