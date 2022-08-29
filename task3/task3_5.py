# 5. Create a new list which contains the specified numbers after removing the even numbers from a
# predefined list

predefined_list = [4, 7, 13, 88, 46, 28, 40, 9, 1, 2]
result = []

for i in predefined_list:
    if i % 2 != 0:
        result.append(i)
print(result)
