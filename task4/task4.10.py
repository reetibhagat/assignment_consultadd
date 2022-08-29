# Write a program which uses filter() to make a list whose elements are even numbers between 1
# and 20 (both included)

list_1 = range(1, 21)
print(list(filter(lambda x: x % 2 == 0, list_1)))
