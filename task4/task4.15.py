# 15. Write a program in Python to multiply the elements of a list by itself using a traditional function
# and pass the function to map() to complete the operation.
def mulSqaure(n):
     return(n*n)
list_1 = range(1,10)
print(list(map(mulSqaure,list_1)))