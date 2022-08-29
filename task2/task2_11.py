# 11. In the previous question, insert break after the “Good guess!” print statement. break will terminate
# the while loop so that users do not have to continue guessing after they found the number. If the user
# does not guess the number at all, print “Sorry but that was not very successful”

counter = 1
luck_number = 7

while counter <= 5:
    user_input = eval(input("Enter the number: "))
    counter += 1
    if (user_input == luck_number):
        print("Good guess!")
        break
    elif counter <= 5:
        print("Try again!")
print("Sorry but that was not very successful")