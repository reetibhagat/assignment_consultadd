# 2. Write a function that accepts a string and prints the number of uppercase letters and lowercase
# letters.
# Sample input: “abcSdefPghijQkl”
# Expected Output: No. of Uppercase characters : 3 No. of Lower case Characters : 12

input_value = "abcSdefPghijQkl"

upper_count = 0
lower_count = 0


def letter():
    global upper_count
    global lower_count
    for i in input_value:
        if i.isupper():
            upper_count += 1
        else:
            lower_count += 1


letter()
print("No. of Uppercase characters : ", upper_count)
print("No. of Lower case Characters : ", lower_count)

