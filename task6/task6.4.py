# 4. Write a program in Python using generators to reverse the string.
# Input String = “Consultadd Training”

input_string ="Consultadd Training"
def reverse_s(input_string):
    for i in range(len(input_string)-1, -1, -1):
        yield input_string[i]

a= reverse_s(input_string)
print(a.__next__())
print(a.__next__())
print(a.__next__())

for i in a:
    print(i)