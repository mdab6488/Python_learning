def logtime(func):
    def wrapper():
        # do something before the function call
        print("Before the function call")
        val = func()
        print("After the function call")
        # do something after the function call
        return val

    return wrapper


@logtime
def hello():
    print("Hello, World!")


hello()
