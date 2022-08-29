# 6. Write a program in Python to iterate through the string “hello my name is abcde” and print the
# string which is having an even length.
string ="hello my name is abcd"
list_s = string.split(' ')
print(list_s)
even_string =[]
for i in list_s:
    if len(i)%2 == 0:
        even_string.append(i)
print(even_string)