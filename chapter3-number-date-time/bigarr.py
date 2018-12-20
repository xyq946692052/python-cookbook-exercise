import numpy

ax = numpy.array([1,2,3,4,5])
ay = numpy.array([4,5,6,7,8])
print(ax * 2)
print(ax + 10)
print(ax + ay)
print(numpy.sqrt(ax))
print(numpy.cos(ax))

grid = numpy.zeros(shape=(10000, 10000), dtype=float)
print(grid)
print(grid+10)
print(numpy.sin(grid))

a = numpy.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(a)
print(a[1])
print(a[:,1])

print(a[1:3, 1:3])
print(a[1:3,1:3]+10)
print(a+[100,111,222,333])
print(numpy.where(a<10,a,10))
