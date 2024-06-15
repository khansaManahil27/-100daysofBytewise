def is_prime(number):
    if number <= 1:
        return f"{number} is not a prime number."
    elif number == 2:
        return f"{number} is a prime number."
    elif number % 2 == 0:
        return f"{number} is not a prime number."
    
    for i in range(3, int(number**0.5) + 1, 2):
        if number % i == 0:
            return f"{number} is not a prime number."
    
    return f"{number} is a prime number."

# Test the function
input_number = 7
print(is_prime(input_number))  # Output: 7 is a prime number.

input_number = 10
print(is_prime(input_number))  # Output: 10 is not a prime number.