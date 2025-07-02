print()
with open(r"C:\00_MDAB\Learning\Python_learning\04.  Coding With Sagar\10_File_Handling\data.txt", "w") as f:
    content = input("Enter content to write = ")
    f.write(content)
    print("Saved!")
