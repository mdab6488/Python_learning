# Match-case statement (switch): An alternative to using many "elif" statements
#                                Execute some code if a value matches a 'case'
#                                Benefits: cleaner and syntax are more readable

# def day_of_week(day):
#     if day == 1:
#         return "It is sunday"
#     elif day == 2:
#         return "It is Monday"
#     elif day == 3:
#         return "It is Tuesday"
#     elif day == 4:
#         return "It is Wednesday"
#     elif day == 5:
#         return "It is Thursday"
#     elif day == 6:
#         return "It is Friday"
#     elif day == 7:
#         return "It is Saturday"
#     else:
#         return "Not a valid day"
#
# print(day_of_week(3))

def day_of_week(day):
    match day:
        case 1:
            return "It is Saturday"
        case 2:
            return "It is Sunday"
        case 3:
            return "It is Monday"
        case 4:
            return "It is Tuesday"
        case 5:
            return "It is Wednesday"
        case 6:
            return "It is Thursday"
        case 7:
            return "It is Friday"
        case _:
            return "Not a valid day"

print(day_of_week(1))

def is_weekend(day):
    match day:
        case "Sunday" | "Monday" | "Tuesday" | "Wednesday" | "Thursday":
            return False
        case"Friday":
            return True
        case _:
            return False

print(is_weekend("Friday"))