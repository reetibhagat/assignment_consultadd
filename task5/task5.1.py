# 1. Write a program in Python to allow the error of syntax to be handled using exception handling.
# HINT: Use SyntaxError


def n():
    try:
        eval('a=====b')
    except SyntaxError:
        print("There is syntax error")
n()
