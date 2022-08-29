# 5. Write a program in Python to reverse a string and print only the vowel alphabet if it exists in the
# string with their index.
def reverse_vowels(str1):
    vowels = ""
    for char in str1:
        if char in "aeiouAEIOU":
            vowels += char
    for i in range(len(vowels)-1, -1, -1):
          print("index:",i,"vowels:", vowels[i], end=" ")

reverse_vowels("apple")
