import numpy
m = numpy.matrix([[1,-2,3],[0,4,5],[7,8,-9]])
print(m)
print(m.T,m.I)

v = numpy.matrix([[1],[2],[3]])
print(v)
print(m*v)
