# 10. Generate and print another tuple whose values are even numbers in the given tuple
# # (1,2,3,4,5,6,7,8,9,10).

tup = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
list1 = list()

for t in tup:
    if t % 2 == 0:
        list1.append(t)
tp1 = tuple(list1)
print(tp1)
