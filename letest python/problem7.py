# create a class "program" for stopping information of few programs working g at microsoft.

class Programmer:
    company = "Microsoft"
    def __init__(self, name, salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin

p = Programmer("Anjali", 12000000, 245001) 
print(p.name, p.salary, p.pin, p.company)
r = Programmer("Rahul", 12000000, 245001)
print(r.name, r.salary, r.pin, r.company)


# Write a class "Calculator" capable of finding square , cube and square root of a number.
class Calculator:
    def __init__(self, n):
        self.n = n

    def Square(self) :
        print(f"the square is {self.n*self.n}")   

    def Cube(self) :
        print(f"the cube is {self.n*self.n*self.n}")  

    def SquareRoot(self) :
        print(f"the squareRoot is {self.n**1/2}")

    @staticmethod
    def hello():
        print("Hello there!")

a = Calculator(4)   
a.hello()               
a.Square()
a.Cube()
a.SquareRoot()

#Create a clas with a class attribute  ; create an object from it and set 'a'
# directly using object.a = 0 does this change the clas attribute ?

class Demo:
    a = 4

o = Demo()

print(o.a) # prints the class attribute because instance attribute ia not present

o.a = 0  # Instance attribute is set

print(o.a) # prints the class attribute because instance attribute ia present

print(Demo.a) # prints the class attribute

# Write a class Train which has methods to book a ticket ,get  status (not a seats)and 
# get fare information of Train running under Indian Railways. 
from random import randint
class Train:
    def __init__(self, trainNo):
        self.trainNo = trainNo

    def book(self, fro, to):
        print(f"Ticket is booked in train no: {self.trainNo} from {fro} to {to} ")

    def getStatus(self) :
        print(f" train no: {self.trainNo} is running on time ")
        
    def getFare(self, fro, to):
        print (f"Ticket fare in train no: {self.trainNo} from {fro} to {to} is {randint(222, 5555)}")

t = Train(12399)
t.book("Allahabad", "Delhi")
t.getStatus()
t.getFare("Allahabad", "Delhi")
