# WAP to ask the user to enter names os their 3 favorite movies & store them in a list
movies = []
mov = input("enter 1st movie:")
movies.append(mov)
mov = input("enter 1st movie:")
movies.append(mov)
mov = input("enter 1st movie:")
movies.append(mov)

print(movies)

# WAP to check if a list contains a palindrome of elements .
list1 = ['1','2','1']
list2 = [1,2,3]

copy_list1 = list1.copy()
copy_list1.reverse()

if copy_list1 == list1:
    print("palindrome")
else:
    print("not palindrome")

# WAP to count the number of students wih the 'A' grade in the following tuple.

grade = ("C","D","A","A","B","B","A")
print(grade.count("A"))

# Store the above values in a list & sort them from "A" to "D".
grade = ["C","D","A","A","B","B","A"]
grade.sort()
print(grade)
