# 3. Learn More about Yield, next and Generators
def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1
a= infinite_sequence()
print(a.__next__())
print(a.__next__())
print(a.__next__())
for i in a:
    print(i)