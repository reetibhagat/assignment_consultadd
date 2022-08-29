# 7. Define a function that can accept two strings as input and print the string with the maximum length
# in the console. If two strings have the same length, then the function should print both the strings line
# # by line.

a= input('Enter the first name:')
b=input('Enter the second name:')

def  max_len(a,b):
    if len(a)== len(b):
        print(a,b ,sep='\n')
    elif len(a) > len(b):
        print(a)
    else:
        print(b)

max_len(a,b)