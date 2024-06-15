def are_anagrams(str1, str2):
    # Clean the strings by removing spaces and converting to lowercase
    cleaned_str1 = ''.join(char.lower() for char in str1 if char.isalnum())
    cleaned_str2 = ''.join(char.lower() for char in str2 if char.isalnum())
    
    # Sort the characters in each string and compare
    if sorted(cleaned_str1) == sorted(cleaned_str2):
        return f"{str1} and {str2} are anagrams."
    else:
        return f"{str1} and {str2} are not anagrams."

# Test the function
input_str1 = "listen"
input_str2 = "silent"
print(are_anagrams(input_str1, input_str2))  # Output: listen and silent are anagrams.

input_str1 = "python"
input_str2 = "java"
print(are_anagrams(input_str1, input_str2))  # Output: python and java are not anagrams