from array import *

arr = array('i', [1, 2, 1, 5])

for a in arr:
    print(a)
# copy the array

newArray = array(arr.typecode, (a for a in arr))

# print copied array

for n in newArray:
    print(n)

# Array values from users

count = int(input("Enter the number of values"))

userarr = array('i', [])

for n in range(count):
    val = int(input("Enter the values"))
    userarr.append(val)

for n in userarr:
    print(n)