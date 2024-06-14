def check_even_or_odd(number):
    if number % 2 == 0:
        return f"{number} is even"
    else:
        return f"{number} is odd"

# Get the number from the user
number = int(input("Enter a number: "))

# Check if the number is even or odd
result = check_even_or_odd(number)

# Print the result
print(result)