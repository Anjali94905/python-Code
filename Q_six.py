
# (Q1) print numbers from 1 to 100.

Number = 1
while Number <= 100:
    print(Number)
    Number += 1
# (Q2) Print number from 100 to 1.
Number = 100
while Number >= 1:
    print(Number)
    Number -= 1

# (Q3) Print the multiplication of a number n.
n = int(input("enter number:"))
i = 1
while i<= 10:
    print(n*i)
    i+=1

# (Q4) print the elements of the following list using a loop.
heroes = ["ironman", "thor", "superman", "batman"]
idx = 0
while idx < len(heroes):
    print(heroes[idx])
    idx += 1

nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
idx = 0
while idx < len(nums):
    print(nums[idx])
    idx += 1

#(Q5) search for a number x in this tuple using loop.

nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 36)

x = 36
i = 0
while i < len(nums):
    if nums[i] == x:
        print("found at idx",i)
    i += 1
else:
    print("finding...")
i += 1

# (Q6) print the elements of the following list using a loop:
#[1, 4, 16, 25, 36, 49, 64, 81, 1000]
nums = [1, 4, 16, 25, 36, 49, 64, 81, 1000]

for el in nums:
    print(el)

# (Q7) search for a number x in tuple using loop:
#[1, 4, 16, 25, 36, 49, 64, 81, 1000, 49]
nums = (1, 4, 16, 25, 36, 49, 64, 81, 1000, 49)
x = 49
idx = 0
for el in nums:
    if el == x :
        print("number found at idx", idx)
        break
    idx += 1

# Range
# (Q8)print numbers from 1 to 100.
for i in range(1,101):
        print(i),
# (Q9)  print numbers from 100 to 1.
for i in range(100,0,-1 ):
       print(i)
# (Q10) print the multiplication table of a number n.
n = int(input("enter number:"))
for i in range(1,11):
    print(n*i)
# (Q11) WAP to find the sum of first n natural number  0
num = 7
add = 0
i = 1
while i <= num:
    add +=i
    i += 1
print("total sum =",add)

# (Q12) WAP to find the factorial of first n numbers.
num = 5
fact = 1
for i in range (1 , num+1):
    fact *= i
print("factorial =",fact)

