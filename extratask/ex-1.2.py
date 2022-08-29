# 2. Create a list of thousand numbers using range and xrange and see the difference between each
# other.
# (For reference:https://www.techbeamers.com/python-xrange-range/)

a = range(1, 1000)
# b = xrange(1, 1000)
#  In Python 3, there is no xrange ,
#  but the range function behaves like xrange in Python 2
print(type(a))
# print(type(b)