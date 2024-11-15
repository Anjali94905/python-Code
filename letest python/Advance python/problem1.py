# WAP TO INPUT NAME ,MAKE and phone number of a student and format it using format function.

name = input("Enter name: ")
marks = int(input("Enter marks: "))
phone  = int(input("Enter number : "))

s = "The name of the student is {} , his marks are {} and phone number is {}".format(name, marks, phone)

print(s)

# A list contains the multiplication table of 7 write a program to convert it to vertical string of same numbers.

table = [str(7*i) for i in range(1, 11)]

s = "\n".join(table)
print(s)

# Write a program to filter a list of numbers which are division by 5.

def divisibale5(n):
    if n%5 == 0 :
        return True
    return False
a = [1, 3, 234, 4321, 543, 678, 987, 5643, 55, 45]
f = list(filter(divisibale5, a))
print(f)
'''
# WAP to find the maximum of the number of the numbers in a list using the reduce function.
'''
from functools import reduce
l = [1, 3, 234, 4321, 543, 678, 987, 5643, 55, 45]

def greater(a, b):
    if a>b :
        return a
    return b
print(reduce(greater, l))

