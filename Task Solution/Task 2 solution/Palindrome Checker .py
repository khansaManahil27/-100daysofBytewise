def is_palindrome(word):
    # Convert the word to lowercase to make the check case-insensitive
    word = word.lower()
    # Reverse the word and compare with the original
    if word == word[::-1]:
        return f"{word} is a palindrome."
    else:
        return f"{word} is not a palindrome."

# Test the function
input_word = "racecar"
print(is_palindrome(input_word))  # Output: racecar is a palindrome.

input_word = "Python"
print(is_palindrome(input_word))  # Output: Python is not a palindrome.