# Get the first number from the user
first_number = float(input("Enter first number: "))

# Get the second number from the user
second_number = float(input("Enter second number: "))

# Get the operation from the user
operation = input("Enter operation (+, -, *, /): ")

# Perform the operation and calculate the result
if operation == '+':
    result = first_number + second_number
elif operation == '-':
    result = first_number - second_number
elif operation == '*':
    result = first_number * second_number
elif operation == '/':
    if second_number != 0:
        result = first_number / second_number
    else:
        result = "undefined (division by zero)"
else:
    result = "Invalid operation"

# Print the result
print(f"The result is: {result}")