def calculate_average(numbers):
    total = sum(numbers)
    return total / len(numbers)

nums = [10, 20, 30, 40]
print("the average is:", calculate_average(nums))