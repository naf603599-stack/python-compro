def display_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

display_info(name="Siriyaporn", age=20, city="Uttaradit")
#Output:
# name: Siriyaporn
# age: 20
# city: Uttaradit