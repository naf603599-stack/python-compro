def divide (a,b):
    try :
        result = a/b
    except ZeroDivisionError as e :
        print("Exception: ",e)
    else:
        return result

a,b=map(int,input("enter two numbers separated by space: ").split())
print(f"The result of {a} divideed by {b} is : {divide(a,b)}")
print("End of program")