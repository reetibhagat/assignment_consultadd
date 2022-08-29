# 2. Define a class named Shape and its subclass Square. The Square class has an init function which
# takes length as argument. Both classes have an area function which can print the area of the shape
# where Shape’s area is 0 by default.

class shape:
    def __init__(self):
        pass

    def area(self):
        print(0)


class square(shape):
    def __init__(self, length):
        self.length = length
        super(square, self).__init__()

    def area(self):
        a = (self.length * self.length)
        print('The area of a square with a side length of %f is %f' % (self.length, a))


s = square(2)
s.area()


