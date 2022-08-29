# 2. Write a program in Python to perform the following operator based task:
# Ask user to choose the following option first:
# If User Enter 1 - Addition
# If User Enter 2 - Subtraction
# If User Enter 3 - Division
# If User Enter 4 - Multiplication
# If User Enter 5 - Average
# Ask user to enter two numbers and keep those numbers in variables num1 and num2
# respectively for the first 4 options mentioned above.
# Ask the user to enter two more numbers as first and second for calculating the average as
# soon as the user chooses an option 5.
# At the end if the answer of any operation is Negative print a statement saying “NEGATIVE”
# NOTE: At a time a user can only perform one action.


options = int(input("enter the options 1-5 :"))


def operation(options):
    global num1, num2, num3, num4
    if options == 1 or options == 2 or options == 3 or options == 4 or options == 5:
        num1 = int(input("enter the number :"))
        num2 = int(input("enter the number :"))
    elif options == 5:
        num3 = int(input("enter the number :"))
        num4 = int(input("enter the number :"))
    if options == 1:
        ans = (num1 + num2)
        if ans > 0:
            print(ans)
        else:
            print("NEGATIVE")
    elif options == 2:
        ans = (num1 - num2)
        if ans > 0:
            print(ans)
        else:
            print("NEGATIVE")
    elif options == 3:
        ans = (num1 / num2)
        if ans > 0:
            print(ans)
        else:
            print("NEGATIVE")
    elif options == 4:
        ans = (num1 * num2)
        if ans > 0:
            print(ans)
        else:
            print("NEGATIVE")
    elif options == 5:
        ans = (num1 + num2 + num3 + num4 / 4)
        if ans > 0:
            print(ans)
        else:
            print("NEGATIVE")


operation(options)
