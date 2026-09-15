try:
    value=int(input("Enter a number: "))
    result=10/value
except ValueError:
    print(" Invalid input! Please enter a valid integer.")
except ZeroDivisionError:
    print("Divission br zero is not allowed.Please enter a non-zero integer.")
else:
    print(f"The result of 10 divided by {value} is: {result}")
finally:
    print("Execution of the try-except block is completed.Program Continues.")

print("END OF PROGRAM")