# Write a function to compute 5/0 and use try/except to catch the exceptions

def div_n(n):
    try:
       k = n/0
    except ZeroDivisionError:
        print("can't divide by zero")
    finally:
        print("This is finally executed")
div_n(5)
