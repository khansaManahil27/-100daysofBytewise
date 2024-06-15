def list_of_squares(n):
    return [i**2 for i in range(1, n + 1)]

# Create a list of squares of the first 10 integers
squares = list_of_squares(10)
print(squares)  # Output: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]