# WAP to input users first name & print its length.
name = input("enter your name:")
print("length of your name is " , len(name))

# WAP to find the occurrence of  '$' in a string.
my_Str = "Hii , $ I am the $ symbol $99.99"
print(my_Str.count("$"))

# WAP to check if a number entered by the user is odd or even.
num = int(input("enter number:"))
rem = num % 2
if rem == 0:
    print("Even")
else:
    print("Odd")

# WAP to find the greatest of 3 numbers entered by the user.
a = int(input("enter first number:"))
b = int(input("enter second number:"))
c = int(input("enter third number:"))

if a >= b and a >= c :
    print("first number is largest", a)
elif b >= c :
    print("second number is largest",b)
else:
    print("third is largest",c)

# WAP to check if a number is a multiple of 7 or not.
x = int(input("enter number:"))

if x % 7 == 0 :
    print("multiple of 7")
else:
    print("not a multiple")
