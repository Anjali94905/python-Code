# (Q1) Create student class that takes name & marks of 3 subjects as arguments in constructor.Then create a method to print the average.

class Student:
    
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    
    
    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("Hi", self.name, "your avg score is:", sum/3)

s1 = Student("Anjali",[99 ,98, 97])
s1.get_avg()

s1.name = "Sona Singh"
s1.get_avg()

# This is a "Abstraction".
class car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False

    def start(self):
       self.clutch = True
       self.acc = True
       print("car started...")

car1 = car()
car1.start() 
 
# (Q2) Create Account class with 2 attributes - balance & account no. Create methods for debit,credit & printing the balance.
class Account:
    def __init__(self, bal, acc):
         self.balance = bal
         self.account_no = acc

# debit method
    def debit(self, amount):
       self.balance -= amount
       print("Rs,", amount, "was debited")
       print("total balance = ", self.get_balance())

# credit method
    def credit(self, amount):
       self.balance += amount
       print("Rs,", amount, "was credited ")
       print("total balance = ", self.get_balance())

    def get_balance(self) :
       return self.balance   

acc1 = Account(10000, 12345)
acc1.debit(1000)
acc1.credit(500)
acc1.credit(1000000)