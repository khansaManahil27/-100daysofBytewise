def is_palindrome(s):
    # Remove spaces and convert to lowercase for case insensitivity
    clean_string = s.replace(" ", "").lower()
    
    # Initialize pointers for the beginning and end of the string
    left, right = 0, len(clean_string) - 1
    
    # Loop through the string from both ends towards the center
    while left < right:
        if clean_string[left] != clean_string[right]:
            return False
        left += 1
        right -= 1
    
    return True

# Get the string from the user
user_string = input("Enter a string: ")

# Check if the string is a palindrome
if is_palindrome(user_string):
    print(f"{user_string} is a palindrome")
else:
    print(f"{user_string} is not a palindrome")
    