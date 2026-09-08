keep_going = 'y'
while keep_going == 'y':
    wholesalecost = float(input("Enter the item's wholesale cost:"))
    retailprice=wholesalecost*2.5
    print(f'Retail price : ${retailprice : .2f}')
    keep_going = input('Do you have another item?'+\
                       ' commission (Enter y for yes): ')