# 4 Write a program in Python to break and continue if the following cases occurs:
# If user enters a negative number just break the loop and print “It’s Over”
# If user enters a positive number just continue in the loop and print “Good Going”
while True:
    user_input = eval(input("Enter any number: "))
    if (user_input < 0):
        print("It's Oveer")
        break
    else:
        print("Good Going")
