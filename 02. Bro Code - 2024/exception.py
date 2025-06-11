# exception = An event that interrupts that flow of a program
#             (ZeroDivisionError, TypeError, ValueError)
#             1. try, 2. except, 3. finally

# 1 / 0 # ZeroDivisionError
# 1 + "1" # TypeError
# int("pizza") # ValueError

# try:
#     # Try some code
#     pass
# except ZeroDivisionError: # Exception
#     # Handle and Exception
#     pass
# finally:
#     # Do some cleanup
#     pass

try:
    number = int(input("Enter a number: "))
    print(1 / number)
except ZeroDivisionError:
    print("You can't divide by zero IDIOT!")
except ValueError:
    print("Enter only numbers please!")
except Exception:
    print("Something went wrong!")
finally:
    print("Do some cleanup here")

