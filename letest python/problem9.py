#WAP to print third, fifth and seventh element from a list using enumerate function.
l = [1, 2, 3, 4, 5, 6, 7, 8]
for i, item in enumerate(l):
    if i == 2  or i == 4 or i == 6:
        print(item)

# write a list comprehension to print a list which contains the multiplication table or a user entered no. 

n = int(input("enter a number: "))

table = [n*i for i in range(1, 11)]
print(table)

# WAP to display a/b where a and b are integers. if b=0 ,display infinite by handling the ZeroDivisionError.

try:
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    print(a/b)
    
except ZeroDivisionError as v :
    print("Infinite")

# Store the multiplication tables generated in problem 3 in a file named tables txt.

n = int(input("enter a number: "))

table = [n*i for i in range(1, 11)]
with open("table.txt","a")as f :
    f.write(f"Table of {n}: {str(table)}  \n")
    
    
