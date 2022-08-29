# 8. Define a function which can generate and print a tuple where the values are square of numbers
# between 1 and 20 (both 1 and 20 included).
def square_num(n):
    list_1 = []
    for i in range(1,n+1):
        a= i*i
        list_1.append(a)
    return(list_1)

print(tuple(square_num(30)))