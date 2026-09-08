def find_max(*args):
    if not args:
        return None
    max_value = args[0]
    for num in args:
        if num > max_value:
            max_value = num
    return max_value

#Example usage
result = find_max(3, 5, 9, 2, 8)
print(f"The maximum value is: {result}")  # Output: The maximum value is: 9 

#Example usage
result = find_max()
print(f"The maximum value is: {result}")  # Output: The maximum value is: None
