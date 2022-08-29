# 5. Write an example on decorators.

def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print("wrapper function is executed before {}".format(original_function.__name__))
        return original_function(*args, **kwargs)
    return wrapper_function

@decorator_function
def display():
    print("This is an display function")

display()

@decorator_function
def sum(a,b):
    print(a+b)
sum(3,3)
