class Vector:
    def __init__(self, list_number):
        self.list_number = list_number

    def __len__(self):
        return len(self.list_number)

print()
# Test the implementation
v1 = Vector([1, 2, 3])
print(len(v1))