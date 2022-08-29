# 4. Write a program in Python to iterate through the list of numbers in the range of 1,100 and print
# the number which is divisible by 3 and is a multiple of 2.


def nums():
    list_n =[]
    for i in range(1, 101):

        if i % 3 == 0 and i % 2 == 0:
            list_n.append(i)

    print(list_n)

print("The number which is divisible by 3 and is a multiple of 2:")
nums()


