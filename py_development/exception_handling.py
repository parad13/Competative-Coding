try:
    x = 1/0
except ZeroDivisionError:
    print("Cannot divide by zero")
else: 
    print("Else case")
finally:
    print("This will always execute")