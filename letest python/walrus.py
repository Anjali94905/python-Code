# Using walrus operator
if (n := len([1, 2, 3, 4, 5])) > 3:
    print(f"List is too long ({n} elements, expected <= 3)")
    # Output: List is too long (5 elements, expected <= 3)

# match_case statement

def http_status(status):
    match status:
        case 200:
            return "OK"
        case 404:
            return "Not Found"
        case _:
            return "Unknown status"

print(http_status(5007))    

# Exception handling

try:
    a = int(input("Hey, Enter a number: "))
    print(a)
except ValueError as V:
    print("Hey")
    print(V)  
except Exception as e:
    print(e)    
print("Thank you")    

#ZeroDivisionError
a = int(input(" Enter a number: "))
b = int(input(" Enter a number: "))

if b == 0 :
    raise ZeroDivisionError("Hey our program is not meant to divide numbers by zero")

else:
    print(f"The division a/b is {a/b}")

# finally

def main():
    try:
        a = int(input("hey , enter a number"))
        print(a)
        return
    
    except Exception as a:
        print(a)
        return
    
    finally:
        print("Hey i am inside of finally")

main()  

#Global a 
a = 89
def fun():
    a = 3
    print(a)

fun()
print(a)

#enumerate  
l = [3, 513, 53, 535]
for index , item in enumerate(l) :
    print(f"The item number at index {index} is {item}")

#list comprehensions  
myList = [1, 2, 9, 5, 3, 5]
squaredList = [i*i for i in myList]

print(squaredList)