#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculates the factorial of a given non-negative integer.

    Parameters:
    n (int): The non-negative integer whose factorial is to be calculated.

    Returns:
    int: The factorial of the given integer. Returns 1 if n is 0.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Get the argument from the command line, calculate its factorial, and print the result.
f = factorial(int(sys.argv[1]))
print(f)
