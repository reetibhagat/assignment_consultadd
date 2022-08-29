# 8. Write a program that accepts a string as an input from the user and calculate the number of digits
# and letters.
# Sample input: consul72
# Expected output: Letters 6 Digits 2

letter_count = 0
digit_count = 0
user_input = str(input("Enter your input: "))

for i in user_input:
    try:
        int(i)
        digit_count += 1
    except:
        letter_count += 1

print("Digit Count: ", digit_count)
print("Letter Coount: ", letter_count)
