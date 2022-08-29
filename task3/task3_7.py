# 7. Write a program to replace the last element in a list with another list.
# Sample input: [1,3,5,7,9,10], [2,4,6,8]
# Expected output: [1,3,5,7,9,2,4,6,8]

list_1 = [1, 3, 5, 7, 9, 10]
list_2 = [2, 4, 6, 8]
list_1.remove(list_1[-1])
result = list_1 + list_2
print(result)
