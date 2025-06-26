from sys import argv, exit

# python _sys.py Alamin
# hello, my name is Alamin

print()

# try:
#     print("hello, my name is:", argv[1])
#     print("Hello, my name is:", argv[1], argv[2])
# except IndexError:
#     print("Too few arguments")

# # Check for errors
# if len(argv) < 2:
#     print("Too few arguments")
# elif len(argv) > 2:
#     print("Too many arguments")
#
# # Print name tags
# print("Hello, my name is:", argv[1])

if len(argv) < 2:
    exit("Too few arguments")
# elif len(argv) > 2:
#     exit("Too many arguments")

# print("Hello, my name is:", argv[1])
for arg in argv[1:]:
    print("Hello, my name is:", arg)




