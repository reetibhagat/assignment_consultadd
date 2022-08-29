# 6. Create a list of elements such that it contains the squares of the first and last 5 elements between
# 1 and 30 (both included).

data_list = []

for i in range(1, 31):
    if i == 1:
        data_list.append(i * i)
    if i > 25:
        data_list.append(i * i)

print(data_list)
