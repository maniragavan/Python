from Inheritance import *

# Iterator
nums = [1, 3, 5, 9, 4]

ite = iter(nums)

print(ite)

print(ite.__next__())
print(ite.__next__())

print(next(ite))

print('iterator class ')
class IterClass:

    def __init__(self):
        self.num = 1

    def __iter__(self):
        return self

    def __next__(self):

        if self.num < 10:
            val = self.num
            self.num += 1

            return val
        else:
            raise StopIteration

ite = IterClass()

for i in ite:
    print(i)