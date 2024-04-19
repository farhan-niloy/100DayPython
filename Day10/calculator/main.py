from art import logo

print(logo)


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2

dict = {}

dict['+'] = "add"
dict['-'] = "subtract"
dict['*'] = "multiply"
dict['/'] = "divide"

print(dict)
