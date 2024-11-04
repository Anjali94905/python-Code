# (Q1)  WAP to print multiplication table of a given number using for loop.
n = int(input("Enter a number:  "))


for  i in range(1, 11):
    print(f"{n} x {i} = {n * i}")

# (Q2) calculate the factorial number   

n = int(input("Enter a number:  "))
product = 1
for i in range(1, n+1):

    product = product * i

print(f"The factorial of {n} is {product}")

# (Q3) WAP To print the following star pattern.
'''
for n = 3
  *
 ***
*****

'''
n = int(input("Enter a number:  "))
for i in range(1, n+1):
    print(" "* (n-i), end="")
    print("*"* (2*i-1) , end="")
    print("\n")
#(Q4) WAP to print star pattern.
'''
* * *
*   *     for n = 3
* * *

'''
n = int(input("Enter a number:  "))
for i in range(1, n+1):
    if(i==1) or (i==n):
        print("*"* n, end="")
    else:
        print("*", end="")
        print(" "* (n-2), end="")
        print("*", end="")
    print("")

# (Q5) WAP to print multiplication table of n using for loops in reversed order.
n = int(input("Enter a number:  "))

for i in range(1, 11):
    print(f"{n}x {11 - i } = {n*(11-i)}")
