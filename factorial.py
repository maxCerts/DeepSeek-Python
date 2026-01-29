
def factorial(n):
    """
    Calculate the factorial of a non-negative integer n.

    The factorial of a non-negative integer n is the product of all positive integers less than or equal to n.
    It is defined as:
        n! = n * (n-1) * ... * 1
    For n = 0, the factorial is defined as 1.

    Parameters:
    n (int): A non-negative integer whose factorial is to be calculated.

    Returns:
    int: The factorial of n.

    Raises:
    ValueError: If n is negative.

    Examples:
    >>> factorial(5)
    120
    >>> factorial(0)
    1
    >>> factorial(3)
    6
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    result = 1
    for i in range(1, n+1):
        result *= i
    return result