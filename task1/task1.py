# TASK ONE
# NUMBERS AND VARIABLES

# 1. Create three variables in a single line and assign values to them in such a manner that each one of
# them belongs to a different data type

a, b, c = "Ram", 2, 2.89

# 2. Create a variable of type complex and swap it with another variable of type integer.

a = 1 + 2j
b = 4
a, b = b, a
print(a, b)

# 3.Swap two numbers using a third variable and do the same task without using any third variable.

# Swap two numbers using a third variable
var1 = 10
var2 = 20
temp = var1
var1 = var2
var2 = temp
print(var1, var2)

# do the same task without using any third variable.

var1 = 10
var2 = 20
# code to swap var1 and var2

# var1 becomes 30
var1 = var1 + var2
# var2 becomes 10
var2 = var1 - var2
# var1 becomes 20
var1 = var1 - var2
print("After swapping  var1 =", var1, "var2 =", var2)

# 4. Write a program that takes input from the user and prints it using both Python 2.x and Python 3.x
# Version.

person = input("Enter the person name :")
print("Hello {} !".format(person))

# 5.Write a program to complete the task given below:
# Ask users to enter any 2 numbers in between 1-10 , add the two numbers and keep the sum in another variable called z. Add 30 to z and store the output in variable result and print result as the
# final output.

x = int(input("Enter the number between 1-10 :"))
y = int(input("Enter the number between 1-10 :"))
z = x + y
result = 30 + z
print(result)


# 6.Write a program to check the data type of the entered values.
# HINT: Printed output should say - The data type of the input value is : int/float/string/etc


def check_user_input(input):
    try:
        # Convert it into integer
        val1 = int(input)
        print("Input is an integer number. Number = ", val1)
    except ValueError:
        try:
            # Convert it into float
            val1 = float(input)
            print("Input is a float  number. Number = ", val1)
        except ValueError:
            try:
                # convert it into boolean
                val1 = bool(input)
                print("Input is a boolean . boolean = ", val1)

            except ValueError:
                print("No.. input is not a number. It's a string")


input1 = input("Enter your Age ")
check_user_input(input1)

input2 = input("Enter any number ")
check_user_input(input2)

input2 = input("Enter the last number ")
check_user_input(input2)

# 7. Create Variables using formats such as Upper CamelCase, Lower CamelCase, SnakeCase and
#  UPPERCASE.

PersonName = "Reeti"  # Upper CamelCase
personName = "Reeti"  # Lower CamelCase
person_name = "Reeti"  # SnakeCase
PERSONNAME = "Reeti"  # uppercase

# 8 If one data type value is assigned to ‘a’ variable and then a different data type value is assigned to ‘a’
# again. Will it change the value? If Yes then Why?

a = 2
print(a)
a = 3.1
print(a)
#It can dynamically identify it's datatype.
