# 4. Find the largest and smallest number from a given list.

data = [4, 5, 66, 1, 445, 0, -44, -3, 999, 10]
min = data[0]
max = data[0]
for i in data:
    if min > i:
        min = i
    if max < i:
        max = i

print("min is = ", min)
print("max is = ", max)
