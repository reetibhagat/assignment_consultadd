# 9. Write a program to find out the occurrence of a specific character from an alphanumeric string.
# Sample input: 12abcbacbaba344ab
# Expected output: a=5 b=5 c=2
# NOTE: Make sure to avoid counting the occurrence of numeric values in the string.

input_str = "12abcbacbaba344ab"
print("sample input for occurrence:", input_str)

out_str = {y: input_str.count(y) for y in set(input_str) if y.isalpha()}

print("Expected Output: \n" + str(out_str))