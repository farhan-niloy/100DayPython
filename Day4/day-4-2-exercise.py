import random

persons = input("Give me everybody's names,seperated by a comma. ")

names = persons.split(", ")

rand = random.randint(0, len(names))

gonna_pay = names[rand]

print(f"{gonna_pay} is going to pay for the meal today")
