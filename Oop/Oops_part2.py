# (Q1) Define a Circle class to create a circle with radius r using the constructor.
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 22/7 * self.radius **2

    def perimeter(self):
        return 2 * 22/7 * self.radius
      
c1 = Circle(21)  
print(c1.area())  
print(c1.perimeter())

#(Q2)Define  Employee class with attribute role, department & salary.this class also has a showDetails() method
# create an Engineer class that inherits from EMPLOYEE & has additional attributes : name & age.
class Employee:
    def __init__(self, role, dept, salary):
        self.role = role
        self.dept = dept
        self.salary = salary

    def showDetails(self):
        print("role =", self.role)
        print("dept =", self.dept)
        print("salary=", self.salary)

class Engineer(Employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__("Engineer","IT","75,000")

Eng1 = Engineer("Elon Musk",48)
Eng1.showDetails()

# (Q3) Create a class called Order which stores item & its price.use Dunder function --gt--() to convey that:
#Order1 >Order2 if price of order1> price of order2
class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price

    def __gt__(self, odr2):
        return self.price > odr2.price
    
ord1 = Order("chips",20)
ord2 = Order("tea", 15)

print(ord1 > ord2)