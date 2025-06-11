class JustNotCoolError(Exception):
    pass


x = 2

try:
    raise JustNotCoolError("This just isn't cool, man.")
    # raise Exception("I'm a custom exception!")
    # print(x / 1)
    # if type(x) is not str:
    #     raise TypeError("Only strings are allowed")
except NameError as e:
    print(f"NameError: means {e} is probably undefined")
except ZeroDivisionError:
    print("Please do not divide by zero")
except Exception as e:
    print(f"There is an error: {e}")
else:
    print("No exceptions were raised")
finally:
    print("I'm going to print with or without an error")
