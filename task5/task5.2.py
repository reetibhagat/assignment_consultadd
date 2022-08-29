# 2. Write a program in Python to allow the user to open a file by using the argv module. If the
# entered name is incorrect throw an exception and ask them to enter the name again. Make sure
# to use read only mode.

import sys

try:
    with open(sys.argv[1], 'r') as my_file:
        print(my_file.read())
except FileNotFoundError:
    print("File Not found. Please enter the correct file again.")
