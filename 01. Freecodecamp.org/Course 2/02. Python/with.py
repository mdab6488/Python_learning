filename = "/Users/flavio/test.txt"

# try:
#     file = open(filename, "r")
#     content = file.read()
#     print(content)
# finally:
#     file.close()
#     print("File closed")

with open(filename, "r") as file:
    content = file.read()
    print(content)
