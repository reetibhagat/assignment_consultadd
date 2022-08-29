# 7. Write a program in python to print the pair of numbers whose sum is equal to the result
# number that is let's say 8.
# x=[1,2,3,4,5,6,7,8,9,-1]

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, -1]
n = len(a)


def sum_pair(arr, n, s):
    result = []
    for i in range(0, n):
        for j in range(i + 1, n):
            if (arr[i] + arr[j]  ==  s):
                result.append([arr[i], arr[j]])
    return result


print(sum_pair(a, n, 8))
