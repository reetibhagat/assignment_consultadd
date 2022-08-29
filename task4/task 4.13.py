# Flatten the list [1,2,3,4,5,6,7] into 1234567 using reduce().



from functools import reduce
flatten_list = [1,2,3,4,5,6,7]
a=reduce(lambda total, d: 10 * total + d, flatten_list)
print(a)