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

should_continue = True

while should_continue:
    def perform_operation(operation, num1, num2):
        for operator in operations:
            if operation == operator:
                operation_func = operations[operator]
                calculation = operation_func(num1, num2)
                return calculation


    calculation = perform_operation(modeOperation, num1, num2)
    print(f"{num1} {modeOperation} {num2} = {calculation}")

    continue_option = input("Type 'y' for further calculation: ")
    if continue_option.lower() == 'y':
        operation2 = input("Choose an operation:  ")
        num3 = int(input("Enter the next number: "))

        calculation2 = perform_operation(operation2, int(calculation), num3)
        print(f"{calculation} {operation2} {num3} = {calculation2}")

    else:
        should_continue = False