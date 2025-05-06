# Pyhton file detection

import os
print()
# Relative = folder/test.txt
# Absolute = C:/Users/BroCode/Desktop/test.txt
# file_path = "test.txt"
#
# if os.path.exists(file_path):
#     print(f"The location '{file_path}' exits")
# else:
#     print ("That location desn't exit")

# file_path = "stuff/names.txt"
#
# if os.path.exists(file_path):
#     print(f"The location '{file_path}' exits")
# else:
#     print ("That location desn't exit")

# file_path = "C:/Users/LAPTOP GADGET/Desktop/test.txt"
file_path = "C:/Users/LAPTOP GADGET/Desktop/test"

if os.path.exists(file_path):
    print(f"The location '{file_path}' exits")

    if os.path.isfile(file_path):
        print("That is a file")
    elif os.path.isdir(file_path):
        print("That is a directory")

else:
    print("That location desn't exit")