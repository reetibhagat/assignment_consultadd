# 6. Define a function that can receive two integral numbers in string form and compute their sum and
# print it in the console.
num1 = input("enter first value:")
num2 = input("enter second value:")
def cal_sum(a, b):
    s = int(a) + int(b)
    return s
total= cal_sum(num1, num2)
print("Sum of two values :", total)