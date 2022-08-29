# 1. Write a program that calculates and prints the value according to the given formula:
# Q= Square root of [(2*C*D)/H]
# Following are the fixed values of C and H:
# C is 50.
# H is 30.
# D is a variable whose values should be input to your program in a comma-se`parated sequence.
import math
import constant

input_values = input("Enter the values in a comma-separated sequence:")
split_values = input_values.split(',')


for i in split_values:
    D = int(i)
    Q = math.sqrt((2 * constant.C * D) / constant.H)
    print("For D Value of {} result is {}".format(D, Q))
