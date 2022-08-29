# 4. Create a login page backend to ask users to enter the username and password. Make sure to
# ask for a Re-Type Password and if the password is incorrect give chance to enter it again but it
# should not be more than 3 times.

user_name = input("Enter the username:")
password = input("Enter the password :")

n = 1
while n <= 4:
    try:
        if n == 4:
            raise Exception
        n = n + 1
        retype_password = input("Re-Type password:")
        if password == retype_password:
            break
    except Exception:
        print("You have exhausted all your tries")
        break
