# 8. Write a program in Python to complete the following task:
# Create two lists such as even_list and odd_list
# Ask user to enter a number in the range of 1,50 and make sure if the entered number is
# even, append it to the even_list and if the entered number is odd append it to the odd_list.
# Keep that in mind you can only add 5 items in each list
# Make sure once you enter all the 5 elements, calculate the sum of the list and return the
# maximum of the list.
user_list = [ ]
size = 10
for i in range(0, size):
    num = int(input("enter number between 0 and 50: "))
    if 0 <= num <= 50:
        user_list.append(num)
    else:
        print("please enter again")
print(user_list)

def  max_count(uls):
    even_list = []
    odd_list = []
    count_even = 0
    count_odd = 0
    for k in uls:
        if k % 2 == 0:
            if count_even <= 5:
                even_list.append(k)
                count_even += 1
        elif count_odd <= 5:
            odd_list.append(k)
            count_odd += 1
    if sum(even_list) > sum(odd_list):
        return sum(even_list)
    else:
        return (sum(odd_list))



print(max_count(user_list))
print("even list:", even_list)
print("odd list", odd_list)
