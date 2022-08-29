# 16. What is the output of the following codes:
def foo():
    try:
        return 1
    finally:
        return 2


k = foo()
print(k)


# the output is 2 as finally is always executed .

def a():
    try:
        f(x, 4)

    finally:
       print('after f')
    print('after f?')
a()

#This is throw error as f is not defined.
