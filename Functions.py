from math import *
from functools import reduce


def Greet(a):
    pass   # empty

def sq(num):
    print(sqrt(num))

Greet('GOO')

sq(5)


def retmul(a, b):
    return a * b


# return multiple values


# multiple arguments *

def funMultiParameter(a, *b):
    c = 0
    for i in b:
        c = c + i
    print(c)


# multiple parameter with name **

def multiparameterkeyname(a, **b):
    c = '0'
    for i in b:
        c = c + i
    print(c)


funMultiParameter(1, 5, 6, 8, 9)

multiparameterkeyname(1, f=2, m=5, c=9, s=6, t=5)

# Global Variable

g = 10


def some():
    global g
    g = 15
    x = globals()['g']
    print(x)


some()
print(g)

# Pass list to a function
print('List to function' + '\n')
lst = ['mani', 'ragavan', 'kavi', 'balakrishnan']


def listcount(lst):
    longname = []
    for i in lst:
        if len(i) > 6:
            print(len(i))
            longname.append(i)

    for n in longname:
        print(n)


listcount(lst)

# Factorial function
def fact(n):
    f = 1
    for i in range(1, n+1):
        f = f * i
    print(f)

num = [1,5,6,4,3,8]

even = list(filter(lambda n : n % 2 == 0, num))  # filter
double = list(map(lambda n : n * 2, even))  # Map
sum = reduce(lambda a,b: a+b, even)  # reduce
print('filter even numbers',even)
print('map double numbwers',double)
print('reduce sum numbers',sum)

# decorators change behaviour of existing function

def fun(a,b):
    return a/b

def smart_fun(func):

    def inner(a,b):
        if a < b:
            a,b =b,a
        return func(a,b)
    return inner

fun = smart_fun(fun)

print('Decorator',fun(2,4))

# Special variables

print(__name__)