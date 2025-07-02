print()

my_list = [1,2,3,5,3]
print(f"Before List: {my_list}") # Before List: [1, 2, 3, 5, 3]
my_list[0] = "hello"
print(f"After List: {my_list}") # ['hello', 2, 3, 5, 3]
my_list[0:3] = 10, "Alamin", 50.50
print(f"After List: {my_list}") # [10, 'Alamin', 50.5, 5, 3]
