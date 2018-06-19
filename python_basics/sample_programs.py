# Print numbers in Fibonacci series
def print_fibonacci(upperbound):
    a, b = 0, 1
    while a < upperbound:
        print a
        a, b = b, a + b


print_fibonacci(50)
