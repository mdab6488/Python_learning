"""
burger - function
extra chesse - extra feature

main function > function add
without chanding the main function code
"""
print()
def my_decorator(func):
    def wrapper():
        print("Something is happening befor the function is called")
        func()
        print("Something is hapening after the function is called")
    return wrapper

@my_decorator
def say_hello():
    print("Hello")

say_hello()


