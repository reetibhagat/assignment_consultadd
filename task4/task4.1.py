# 1. Write a program to reverse a string.
# Sample input: “1234abcd”
# Expected output: “dcba4321”
input_value = "1234abcd"


def reverse_string(input_value):
    return input_value[::-1]


print(reverse_string(input_value))

for i in range(len(input_value)-1, -1, -1):
    print(input_value[i], end="")
