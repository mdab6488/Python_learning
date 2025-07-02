def greet(name, city):
    """
    diplaying a hi message to user
    :return:
    """
    print(f"Hi {name} form {city}")

print()
greet("Dhaka", "Riyan") # Wrong
greet("Riyan", "Dhaka") # Right

greet(city="Muksudpur", name="Abdur Rahman") # Right