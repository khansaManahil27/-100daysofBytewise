import string

def is_palindrome_sentence(sentence):
    # Remove spaces and punctuation, and convert to lowercase
    cleaned_sentence = ''.join(char.lower() for char in sentence if char.isalnum())
    
    # Check if the cleaned sentence is a palindrome
    if cleaned_sentence == cleaned_sentence[::-1]:
        return f"{sentence} is a palindrome."
    else:
        return f"{sentence} is not a palindrome."

# Test the function
input_sentence = "A man, a plan, a canal: Panama"
print(is_palindrome_sentence(input_sentence))  # Output: A man, a plan, a canal: Panama is a palindrome.

input_sentence = "Hello, world!"
print(is_palindrome_sentence(input_sentence))  # Output: Hello, world! is not a palindrome.