# 1. Create a list of given structure and get the Access list as provided below:
# x=[100,200,300,400,500,[1,2,3,4,5,[10,20,30,40,50],6,7,8,9],600,700,800]
# Access list: [1, 2, 3, 4]Access list: [600, 700]
# Access list: [100, 300, 500, 600, 800]
# Access list: [[800, 700, 600, [1, 2, 3, 4, 5, [10, 20, 30, 40, 50], 6, 7, 8, 9], 500, 400, 300, 200, 100]]
# Access list: [10]
# Access list: [ ]

x = [100, 200, 300, 400, 500, [1, 2, 3, 4, 5, [10, 20, 30, 40, 50], 6, 7, 8, 9], 600, 700, 800]
l1 = [x[index] for index in [0, 2, 4, 6, 8]]

print("Access List:", x[5][0:4])
print("Access List:", x[-3:-1])
print("Access List:", l1)
print("Access List:", x[::-1])
print("Access List:", x[5][5][0])

