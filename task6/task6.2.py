# 2. Write a program to construct a dictionary from the two lists containing the names of students and
# their corresponding subjects. The dictionary should map the students with their respective subjects.
# Let’s see how to do this using for loops and dictionary comprehension.
#     HINT - Use Zip function also
# Sample input: students = ['Smit', 'Jaya', 'Rayyan'] subjects = ['CSE', 'Networking', 'Operating System']
# Expected output: {‘Smit’ : ’CSE’ , ’Jaya’ : ’Networking’ , ’Rayyan’ : ’Operating System’}


# using zip function
students =['Smit', 'Jaya', 'Rayyan']
subjects=['CSE', 'Networking', 'Operating System']
print(dict(zip(students,subjects)))

# using loop

res = {}
for keys in students:
    for value in subjects:
        res[keys] = value
        subjects.remove(value)
        break
print("resultant dictionary:"+str(res))

# using list comprehension
students =['Smit', 'Jaya', 'Rayyan']
subjects=['CSE', 'Networking', 'Operating System']

data_dict = {key:value for (key,value) in zip(students,subjects)}
print("resultant dictionary:" + str(data_dict))
