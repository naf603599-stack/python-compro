#This program calculate the sum of a series of numbers the user enters
max = 5 #the maximum number
total = 0.0
print('This program calculates the sum of')
print(max,'numbers you will enter.')
for count in range(max):
    number = int(input('Enter a number: '))
    total = total + number
print('The total is' ,total)