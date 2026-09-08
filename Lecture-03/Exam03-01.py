# Input the number of employees from the user
num_employees = int(input("Enter the number of employees: "))
#Check the number of employees and print the appropriate company size
if num_employees < 50:
    print("This is a Small company")
elif num_employees < 250:
    print("This is a Medium-size company")
else:
    print("This is a Large company")