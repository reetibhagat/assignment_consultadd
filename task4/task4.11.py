# 11. Write a program which uses map() and filter() to make a list whose elements are squares of even
# numbers in [1,2,3,4,5,6,7,8,9,10].
# Hints: Use filter() to filter even elements of the given listUse map() to generate a list of squares of the
# numbers in the filtered list. Use lambda() to define anonymous functions.

list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list(map(lambda x: x * x,(filter(lambda x: x % 2 == 0, list_1) ))))
