# 5. Write a Person class with an instance variable “age” and a constructor that takes an integer as a
# parameter. The constructor must assign the integer value to the age variable after confirming the
# argument passed is not negative; if a negative argument is passed then the constructor should set
# age to 0 and print “Age is not valid, setting age to 0”. In addition, you must write the following instance
# methods:
# 1.yearPasses() should increase age by the integer value that you are passing inside the function.
# 2.amIOld() should perform the following conditional actions:I
#    f age is between 0 and <13, print “You are young”.
#    If age is >=13 and <=19 , print “You are a teenager”.
#    Otherwise, print “You are old”.
#
# Sample Input for amIOld():
#     -1
#     4
#     10
#     16
#     18
#     64
#     38
#
#
# Expected Output for amIOld():
#
# Age is not valid, setting age to 0.
# You are young.
# You are young.
# You are a teenager.
# You are a teenager.
# You are old.
# You are old.
# Consider the age variable to be set to 38 then:
# Sample Input for yearPasses(): 4
# Expected Output for yearPasses(): 42

class Person:
    age = 0

    def __init__(self, integer):
        if integer < 0:
            print("Age is not valid, setting age to 0")
        else:
            self.age = integer

    def yearPasses(self):
        self.age += 1

    def amIOld(self):
        if self.age == 0 and self.age < 13:
            print("You are young")
        elif self.age >= 13 and self.age <= 19:
            print("You are a teenager")
        else:
            print("You are old")

a= Person(28)
a.amIOld()
