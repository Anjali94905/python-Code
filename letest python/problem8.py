#property decorators

class Employee:
    a = 1

    @classmethod
    def Show(cls):
        print(f"The class attribute of a is  {cls.a}")
    
    @property
    def name(self):
        return f"{ self.fname} {self.lname}"
    
    @name.setter
    def name (self, value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]


e = Employee()
e.a = 45

e.name = " Anjali "
print(e.name)
e.Show()


# Operator overloading

class Number:
    def __init__(self, n ):
        self.n = n

    def __add__(self, num):
        return self.n + num.n
    
n = Number(1)
m = Number(2)
print(n + m)

# Create a clas (2-D vector) and it to create another class representing a 3-D vector.

class TwoDVector:
    def __init__(self, i, j ):
        self.i = i
        self.j = j
    def show(self):
        print(f"The vector is {self.i}i + {self.j}j ") 

class ThreeDVector(TwoDVector):
    def __init__(self, i, j, k):
        super().__init__(i, j)   
        self.k = k

    def show(self):
        print(f"the vector is {self.i}i + {self.j}j + {self.k}k")

a = TwoDVector(1, 2) 
a.show()
b = ThreeDVector(1, 2, 3)
b.show()

# create a class 'Employee' and add salary and increment properties to it.

class Empolyee:
    salary = 234
    increment = 20
    @property
    def salaryAfterIncrement(self):
        return self.salary + self.salary + (self.increment/100)

    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, salary):
        self.increment = ((salary/self.salary)-1 )*100
e = Empolyee()
e.salaryAfterIncrement = 280.9
print(e.increment)

# Complex number
class Complex:
    def __init__(self, r, i):
        self.r = r
        self.i = i

    def __add__(self, C2):
        return Complex(self.r + C2.r, self.i + C2.i)

    def __mul__(self, C2):
        real_part = self.r * C2.r - self.i * C2.i
        imag_part = self.r * C2.r + self.i * C2.i
        return Complex(real_part, imag_part)

    def __str__(self):
        return f"{self.r} + {self.i}i"    

c1 = Complex(1, 2)
c2 = Complex(3, 4)
print(c1 + c2)
print(c1 * c2)