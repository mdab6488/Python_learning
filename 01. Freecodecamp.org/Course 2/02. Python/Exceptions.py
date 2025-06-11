# try:
#     # some lines of code that may cause an exception
# except <ERROR1>:
#     # code to handle the exception
# except <ERROR2>:
#     # code to handle the exception
# except:
#     # code to handle any other exception
# else:
#     # code to run if no exceptions were raised
# finally:
#     # code that will run no matter what (optional)

# result = 2 / 0
# print(result)

# try:
#     result = 2 / 0
# except ZeroDivisionError:
#     print("You cannot divide by zero")
# finally:
#     result = 1

# print(result)

# try:
#     raise Exception("An error occurred")
# except Exception as e:
#     print(f"An error occurred: {e}")


# class DogNotFoundException(Exception):
#     print("Inside DogNotFoundException")
#     pass


# try:
#     raise DogNotFoundException()
# except DogNotFoundException:
#     print("Dog not found")
