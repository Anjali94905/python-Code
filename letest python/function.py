# function Definition
def avg():
    a = int(input("Enter your number:  "))
    b = int(input("Enter your number:  ")) 
    c = int(input("Enter your number:  "))

    average = (a + b + c)/3
    print(average)
#function call
avg()
print("Thank you Anjali..")
#avg()
#avg()
#avg()
#  function  Argument
def goodday(name, ending):
    print("Good Day," + name)
    print(ending)
    return "done"

a = goodday("Anjali","thank you")
print(a)

# Recursion [factorial(n) = n * factorial(n-1)]

def factorial(n):
    if n==1 or n==0:
        return 1
    return n * factorial(n-1)
n = int(input("Enter a number: "))
print (f"the factorial of this number is : {factorial(n)}")
