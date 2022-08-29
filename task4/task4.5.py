# 5. Write a program that accepts a sequence of lines as input and prints the lines after making all
# characters in the sentence capitalized.
# Sample input: Hello world Practice makes man perfect
# Expected output: HELLO WORLD PRACTICE MAKES MAN PERFECT

sequence_lines = input("Enter  sequence of lines:")

for i in sequence_lines:
    cap_char= i.capitalize()
    print(cap_char, end = "")
