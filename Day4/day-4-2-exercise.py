import random

persons = ["Angela", "Farhan", "Null"]

rand = random.randint(0, 2)


def switch_case(case_value):
    if case_value == 0:
        return "Angela is going to buy the meal today!"
    elif case_value == 1:
        return "Farhan is going to buy the meal today!"
    elif case_value == 2:
        return "Null is going to buy the meal today!"
    else:
        return "Invalid Entry"


result = switch_case(rand)

print(result)