"""
open("file_name.txt", "mode")
"""
file = open("10_File_Handling/file.txt", "r")
content = file.read()
print(content)

file.close()