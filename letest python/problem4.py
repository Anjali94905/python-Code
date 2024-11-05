#(Q1) WAP Using functions to find greatest of three numbers.
def greatest (a, b, c):
    
    if a>b and a>c :
        return a
    elif b>a and b>c :
        return b
    elif c>b and c>a :
        return c
    
a = 1
b = 25
c = 40

print(greatest(a, b, c))  

# (Q2) WAP  Using functions to convert Celsius to Fahrenheit.
def f_to_c (f):
   return 5*(f-32)/9

f = int(input("Enter temperature in F: "))
c = f_to_c(f)
print(f"{round(c , 2)} °C")

# (Q3) Write a python function to  print n lines of the pattern.
def pattern(n):
    if n==0:
       return
    print("*" * n)
    pattern(n-1)

pattern(7)

# (Q4) Write a python function which converts inches to CMs .
def inch_to_cms(inch):
    return inch * 2.54
n = int(input("enter value in inches: "))

print(f"the corresponding value in cms is {inch_to_cms(n)}")