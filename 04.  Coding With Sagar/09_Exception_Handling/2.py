print()
try:
    with open(r"C:\00_MDAB\Learning\Python_learning\04.  Coding With Sagar\09_Exception_Handling\errors.txt", "r") as f:
        content = f.read()
        print(content)

except FileNotFoundError:
    print("Fiel not found")
finally:
    print("File operation complete")