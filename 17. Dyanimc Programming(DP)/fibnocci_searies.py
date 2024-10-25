# Interative approach
def fibonacci_iterative(n):
    fib_series = []
    a, b = 0, 1
    for _ in range(n):
        fib_series.append(a)
        a, b = b, a + b
    return fib_series

# Example usage
num_terms = int(input("Enter the number of terms in the Fibonacci series: "))
result = fibonacci_iterative(num_terms)
print(f"Fibonacci series (first {num_terms} terms): {result}")

# Recursive approach
def fibonacci_iterative(n):
    fib_series = []
    a, b = 0, 1
    for _ in range(n):
        fib_series.append(a)
        a, b = b, a + b
    return fib_series

# Example usage
num_terms = int(input("Enter the number of terms in the Fibonacci series: "))
result = fibonacci_iterative(num_terms)
print(f"Fibonacci series (first {num_terms} terms): {result}")


# Using Generators
def fibonacci_generator(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# Example usage
num_terms = int(input("Enter the number of terms in the Fibonacci series: "))
result = list(fibonacci_generator(num_terms))
print(f"Fibonacci series (first {num_terms} terms): {result}")
