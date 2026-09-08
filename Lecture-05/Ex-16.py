def calculate_stats(numbers):
    total_sum = sum(numbers)
    average = total_sum / len(numbers)
    maximum = max(numbers)
    minimum = min(numbers)
    return total_sum, average, maximum, minimum

#Example usage
numbers = [5, 10, 15, 20, 25]
total, avg, max_val, min_val = calculate_stats(numbers)

print(f"Total Sum: {total}")
print(f"Average: {avg}")
print(f"Maximum: {max_val}")
print(f"Minimum: {min_val}")