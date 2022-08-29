# 3. Write a program to get the sum and multiply of all the items in a given list.
data = [4, 5, 3, 5, 6, 43]
sum = 0
multiply = 1
for i in data:
    sum += i
    multiply *= i
print('sum is :', sum)
print('multiply is : ', multiply)
