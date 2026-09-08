worked_hours=int(input("Enter the number of hours worked: "))
rate_hourly=float(input("Enter the hourly pay rate: "))

if worked_hours>40:
    overtime=worked_hours-40
    pay=40*rate_hourly+overtime*rate_hourly*1.5
else:
    pay=worked_hours*rate_hourly
print(f"The gross pay is: ${pay:.2f}")