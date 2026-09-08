def is_armstrong(number):
    # Convert the number to a string to easily iterate over digits
    num_string = str(number)
    num_digits = len(num_string)
    total = 0

    for digit in num_string:
        total += int(digit) ** num_digits
    if total == number:
        return True
    else:
        return False


#Example usage
print(is_armstrong(153))  # Output: True (1^3 + 5^3 + 3^3 = 153)
print(is_armstrong(9474))  # Output: True (9^4 + 4^4 + 7^4 + 4^4 = 9474)
print(is_armstrong(123))  # Output: False (123 is not an Armstrong number)