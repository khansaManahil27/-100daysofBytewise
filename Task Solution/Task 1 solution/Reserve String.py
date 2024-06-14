# Get the string from the user
user_string = input("Enter a string: ")

# Initialize an empty string for the reversed string
reversed_string = ""

# Loop through the original string in reverse order
for char in user_string:
    reversed_string = char + reversed_string

# Print the reversed string
print(f"The reversed string is: {reversed_string}")