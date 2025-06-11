
print()
def generate_table(n):
    table = ""
    for number in range(1, 11):
        table += f"{n} X {number} = {n * number}\n"

    with open(f"tables/table_{n}.txt", "w") as f:
        f.write(table)


for i in range(2, 21):
    generate_table(i)