

class Person():

    def __init__(self,name1,Age):
        print('init person')
        self.name = name1
        self.age = Age
        self.addr = self.address()

    def biodata(self):
        print('name {} Age {}'.format(self.name, self.age))
        self.addr.Show()

    def __gt__(self, other):
        if self.age > other.age:
            return True
        else:
            return False

    @classmethod
    def getheight(cls):
        return cls.height

    @staticmethod
    def GetPlanetLive():
        return 'earth'

    class address:

        def __init__(self):
            self.location = "trivandrum"
            self.state = 'kerala'

        def Show(self):
            print(self.location , self.state)


    height = 20  # static variable

# inheritance in python

class Employee(Person):
    def __init__(self,Age):
        super().__init__('mnaiS',Age)
        self.designation = 'software engineer'

    def biograph(self):
        super().biodata()


emp1 = Employee(5)
emp2 = Employee(8)

emp1.biograph()

if emp1 > emp2:
    print('done')

