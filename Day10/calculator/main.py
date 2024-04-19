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



operations = {}

operations['+'] = add
operations['-'] = subtract
operations['*'] = multiply
operations['/'] = divide

num1 = int(input("Enter first number: "))
modeOperation = input("Choose an operation:  ")
num2 = int(input("Enter second number: "))


for operator in operations:
    if modeOperation == operator:
        operation = operations[operator]
        calculation = operation(num1, num2)
        print(calculation)
