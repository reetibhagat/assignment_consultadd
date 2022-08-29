# 3. Create a function that takes a list and returns a new list with unique elements of the first list.

list_1 = [2,3,2,4,5,4,5,]
def unique_list(list_1):
    u_list= set(list_1)
    return list(u_list)
print(unique_list(list_1))