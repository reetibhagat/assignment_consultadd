# 14. Write a program in Python to find the values which are not divisible by 3 but are a multiple of 7.
# Make sure to use only higher order functions.

def div(n):
    for i in range(n):
        if (n % 3 != 0) & (n % 7 == 0):
            return (n)


list_1 = range(1, 21)
a = (list(map(div, list_1)))
print(a)
