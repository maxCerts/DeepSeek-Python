def factorial_iterative(n):
    """Calculate factorial using iterative method (loop)"""
    if n < 0:
        return "Error: Factorial is not defined for negative numbers"
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def factorial_recursive(n):
    """Calculate factorial using recursive method"""
    if n < 0:
        return "Error: Factorial is not defined for negative numbers"
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)

def factorial_math(n):
    """Calculate factorial using Python's math module"""
    import math
    if n < 0:
        return "Error: Factorial is not defined for negative numbers"
    return math.factorial(n)

def main():
    print("=" * 50)
    print("FACTORIAL CALCULATOR")
    print("=" * 50)
    
    try:
        # Get input from user
        num = int(input("Enter a non-negative integer: "))
        
        # Calculate using different methods
        result_iterative = factorial_iterative(num)
        result_recursive = factorial_recursive(num)
        result_math = factorial_math(num)
        
        # Display results
        print("\n" + "=" * 50)
        print(f"FACTORIAL OF {num}")
        print("=" * 50)
        
        # Check if there was an error (string returned)
        if isinstance(result_iterative, str):
            print(result_iterative)
        else:
            print(f"Iterative method: {num}! = {result_iterative}")
            print(f"Recursive method: {num}! = {result_recursive}")
            print(f"Math module method: {num}! = {result_math}")
            
            # Show calculation steps for small numbers
            if num <= 10 and num >= 0:
                print(f"\nCalculation steps: {num}! = ", end="")
                steps = " × ".join(str(i) for i in range(1, num + 1)) if num > 0 else "1"
                print(f"{steps} = {result_iterative}")
        
    except ValueError:
        print("Error: Please enter a valid integer.")
    except RecursionError:
        print("Error: Number too large for recursive method. Try iterative or math module method.")
    except OverflowError:
        print("Error: Result too large to compute.")
    
    print("\n" + "=" * 50)

if __name__ == "__main__":
    main()