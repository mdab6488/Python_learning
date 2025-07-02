print()
file = open(r"C:\00_MDAB\Learning\Python_learning\04.  Coding With Sagar\10_File_Handling\file_3.txt", "w")

content = input("Enter a data to write: ")
file.write(content)
print("Data Saved Successfully!")

file.close()