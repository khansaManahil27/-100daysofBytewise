# Get the string from the user
user_string = input("Enter a string: ")

# Define a set of vowels
vowels = set('aeiouAEIOU')

# Initialize a counter for the vowels
vowel_count = 0

# Loop through each character in the string
for char in user_string:
    if char in vowels:
        vowel_count += 1

# Print the number of vowels
print(f"The number of vowels is: {vowel_count}")