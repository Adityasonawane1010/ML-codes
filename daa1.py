def fibonacci(n, steps):
    # Increment step count each time the function is called
    steps[0] += 1
    # Base cases
    if n == 0:
        return 0
    elif n == 1:
        return 1
    # Recursive calculation
    else:
        return fibonacci(n - 1, steps) + fibonacci(n - 2, steps)

# Main function to get Fibonacci number and step count
def fibonacci_with_step_count(n):
    steps = [0]  # List to hold step count as a mutable object
    fib_num = fibonacci(n, steps)
    return fib_num, steps[0]

# Example usage
n = int(input("Enter a number: "))
fib_num, step_count = fibonacci_with_step_count(n)
print(f"Fibonacci number at position {n} is {fib_num}")
print(f"Number of steps taken to compute Fibonacci({n}): {step_count}")
