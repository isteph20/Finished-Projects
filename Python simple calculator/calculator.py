def calculator(operation, num1, num2):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        return num1 / num2
    else:
        return "Invalid Operation"

print("Enter the operation to perform (+, -, *, /): ")
operation = input()
print("Enter the first number: ")
num1 = int(input())
print("Enter the second number: ")
num2 = int(input())

print("Result: ", calculator(operation, num1, num2))
