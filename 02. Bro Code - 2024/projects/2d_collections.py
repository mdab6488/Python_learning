
num_pad = ((1,2,3),
           (4,5,6),
           (7,8,9),
           ("*", 0, "#"))

print(num_pad)

print()

for row in num_pad:
    # print(row)
    for num in row:
        print(num, end=" ")
    print()