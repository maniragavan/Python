from numpy import *
from Functions import *

# import modules
print(fun(6,8))
arr = array([1, 2, 1, 6.0, 1], float)

# get type

print(arr.dtype)

# linspace generate 0 to 15 as 5 values

lin = linspace(0, 15, 5)
print(lin)

logs = logspace(0, 5, 3)
print(logs)

ra = arange(5, 5)
print(ra)

# add values to array

ar = arr + 5
print(ar)

ar = arr.copy()

ma = array([[1, 2, 3],
            [4, 5, 6]])
print(ma.ndim)

# flattern the array

ma2 = ma.flatten()

print(ma2)

# convert single to three dimension array

print(ma2.reshape(3, 2))

m = matrix('1,2,3,4;4,6,8,9;4,8,9,7')

print(m.diagonal())


def func():
    print('function')

func()
print(__name__)