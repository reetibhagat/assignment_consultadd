# TASK TWO
# OPERATORS AND DECISION MAKING STATEMENT

# 1.  Write a program in Python to perform the following operation:

# If a number is divisible by 3 it should print “Consultadd” as a string
# If a number is divisible by 5 it should print “Python Training” as a string
# If a number is divisible by both 3 and 5 it should print “Consultadd - Python Training” as a
# string.


num = int(input("enter the number:"))


def check_multiple(num):
    if num % 5 == 0 and num % 3 == 0:
        print("Consultadd - Python Training")
    elif num % 5 == 0:
        print("Python Training")
    elif num % 3 == 0:
        print("Consultadd")
    else:
        print(None)


(check_multiple(num))

