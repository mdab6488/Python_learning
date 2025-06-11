print()
numbers = []

for i in range(3):
    num = int(input(f"Enter Subject {i + 1} Marks: "))
    numbers.append(num)

print("-" * 30)
for index, mark in enumerate(numbers, start=1):
    print(f"You got in subject {index}: {mark}")

# Assuming each subject is out of 100
obtained_marks = sum(numbers)
total_marks = len(numbers) * 100
total_percentage = (obtained_marks / total_marks) * 100

print("*" * 30)
print(f"Total Percentage: {total_percentage:.2f}%")
print("*" * 30)

if total_percentage >= 40 and numbers[0]>=33 and numbers[1]>=33 and numbers[2]>=33:
    print("✔️ You are pass")
else:
    print("❌ You failed, try again next year!")