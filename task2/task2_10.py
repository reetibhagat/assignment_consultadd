# 10. Write a program that asks five times to guess the lucky number. Use a while loop and a counter,
# such as counter=1
# While counter <= 5:
# print(“Type in the”, counter, “number”
# counter=counter+1
# The program asks for five guesses (no matter whether the correct number was guessed or not). If the
# correct number is guessed, the program outputs “Good guess!”, otherwise it outputs “Try again!”.
# After the fifth guess it stops and prints “Game over!”

counter = 1
luck_number = 7

while counter <= 5:
    user_input = eval(input("Enter the number: "))
    counter += 1
    if (user_input == luck_number):
        print("Good guess!")
    elif counter <= 5:
        print("Try again!")
print("Game over!")
