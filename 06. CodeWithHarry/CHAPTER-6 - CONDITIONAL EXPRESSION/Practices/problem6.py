
print()
marks = int(input("Enter your marks: "))

grade = ""

if 100 >= marks >= 90:
    grade = "Ex"
elif 90 > marks >= 80:
    grade = "A"
elif 80 > marks >= 70:
    grade = "B"
elif 70 > marks >= 60:
    grade = "C"
elif 60 > marks >= 50:
    grade = "D"
elif marks < 50:
    grade = "F"

print(f"Your grade is: {grade}")
