# Get the first number from the user
first_number = float(input("Enter first number: "))

# Get the second number from the user
second_number = float(input("Enter second number: "))

# Get the third number from the user
third_number = float(input("Enter third number: "))

# Find the largest number
if first_number >= second_number and first_number >= third_number:
    largest_number = first_number
elif second_number >= first_number and second_number >= third_number:
    largest_number = second_number
else:
    largest_number = third_number

# Print the largest number
print(f"The largest number is: {largest_number}")