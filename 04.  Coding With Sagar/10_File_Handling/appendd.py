print()
with open(r"C:\00_MDAB\Learning\Python_learning\04.  Coding With Sagar\10_File_Handling\data2.txt", "a") as f:
    content = input("Enter data to append: ")
    f.write(content)
    print("Appended Sucessfully")

