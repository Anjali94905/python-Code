#(Q1) WAP to find the greatest of four numbers entered by user.
a1 = int(input("enter number 1 :  "))
a2= int(input("enter number 2 :  "))
a3 = int(input("enter number 3 :  "))
a4 = int(input("enter number 4 :  "))

if a1>a2 and a1>a3 and a1>a4 :
    print("greatest numbers a1:",a1)

elif a2>a1 and a2>a3 and a2>a4 :
    print("greatest numbers a2:",a2)

elif a3>a1 and a3>a2 and a3>a4 :
    print("greatest numbers a3:",a3)

elif a4>a1 and a4>a2 and a4>a3 :
    print("greatest numbers a4:",a4)

#(Q2) WAPto find out whether a student has password or failed.
marks1 = int(input("enter marks1:"))
marks2 = int(input("enter marks2:"))   
marks3 = int(input("enter marks3:"))

# Check for total percentage
total_percentage =(100*(marks1 + marks2 + marks3))/300

if total_percentage>=40 and marks1>33 and marks2>33 and marks3>33 :
    print("you are pass", total_percentage)

else:
    print("You failed, try again next !", total_percentage)

# (Q3) A spam is defined as a text containing following keywords:
# "Make a lot of money",# "buy now", "subscribe this", "click this". WAPto detect this spams.
''' 
p1 ="Make a lot of money "
p2 = "buy now"
p3 = "subscribe this"
p4 = "click this"

message = input("Enter your comment: ")
if (p1 in message) or (p2 in message) or (p3 in message) or (p4 in message):
    print("This is a spam")

else:
    print("This is not a spam")
    '''
#(Q4) WAP which finds out whether a given name is present or not.
'''l = ["Anjali", "Soname", "Anju", "Sona"]

name = input("Enter your name:")

if name in l :
    print("Your name is in the list")
else:
    print("Your name is not in the list")
'''
#(Q5) WAP to calculate the grade of a student from his name.
marks = int(input("enter your marks:"))

if marks<=100 and marks>=91 :
    grade = "Ex"
elif marks<90 and marks>=81 :
     grade = "A"
elif marks<80 and marks>=71 :
     grade = "B+"
elif marks<70 and marks>=61 :
     grade = "B"
elif marks<60 and marks>=51 :
     grade = "C+"
elif marks<50 :
     grade = "C"

     print("Your grade is :",grade)

#(Q6) WAP which finds out whether a given post is talking about ____ or not.
'''post = input("Enter the post:")

if "rahul".lower() in post.lower() :
    print("This post is talking about Rahul")

else:
    print("This post is not talking about Rahul")'''
