from time import *
from threading import *


class sayhi(Thread):
    def run(self) :
        for i in range(5):
            print("Hi \n")
            sleep(1)
    def sam(self):
        pass


class sayhello(Thread, sayhi):
    def run(self):
        for i in range(5):
            print("Hello \n")
            sleep(1)

t1 = sayhello()
t2 = sayhi()



t1.start()
t2.start()

t1.join()
t2.join()

print('bye')