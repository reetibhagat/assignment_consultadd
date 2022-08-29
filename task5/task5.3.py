# 3. Write a program to handle an error if the user entered a number more than four digits it should
# return “The length is too short/long !!! Please provide only four digits”


try:
    user_input = input("Enter the four digits number:")
    assert len(user_input) == 4
except AssertionError:
    print("The length is too short/long !!! Please provide only four digits")
