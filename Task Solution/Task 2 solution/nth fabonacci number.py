def nth_fibonacci(n):
    if n <= 0:
        return "Input should be a positive integer."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n):
            a, b = b, a + b
        return b

# Test the function
input_n = 10
fibonacci_number = nth_fibonacci(input_n)
print(f"The {input_n}th Fibonacci number is {fibonacci_number}.")