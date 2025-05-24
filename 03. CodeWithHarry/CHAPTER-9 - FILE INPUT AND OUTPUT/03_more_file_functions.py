print()
with open("file.txt", "r") as f:
    # lines = f.readlines()
    # print(lines) # ['Riyan is a good boyfriend\n', 'I want to go to study in abroad\n', 'For study business\n', 'Hopefully I go to france for study']
    # print(type(lines)) # <class 'list'>

    # line1 = f.readline()
    # print(line1, type(line1)) # Riyan is a good boyfriend <class 'str'>
    # print()
    #
    # line2 = f.readline()
    # print(line2, type(line2)) # I want to go to study in abroad <class 'str'>
    # print()
    #
    # line3 = f.readline()
    # print(line3, type(line3)) # For study business <class 'str'>
    # print()
    #
    # line4 = f.readline()
    # print(line4, type(line4)) # Hopefully I go to france for study <class 'str'>
    # print()
    #
    # line5 = f.readline()
    # # print(line5, type(line5)) # <class 'str'>
    # print(line5 == "") # <class 'str'> # True
    # print()

    line = f.readline()
    while line != "":
        print(line)
        line = f.readline()

