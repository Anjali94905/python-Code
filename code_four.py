# store followings in a python dictionary.

dictionary = {
    "cat"  : "a small animal",
    "table" : ["a piece of furniture", "list of facts & figure"]
}

print(dictionary)

# you are given a list of subjects for students . Assume one classroom is required for 1 subject . how many classroom are needed by all students.

subjects = {
    "python", "java", "c++", "python", "javascript",
    "java", "python", "java", "c++", "c"
}

print(len(subjects))

#WAP to enter marks of 3 sunject from the user and store them in a dictionary .
#start with an empty dictionary & add one by one .use subject namee as key &marks a value.

marks = {}

x = int(input("enter phy :"))
marks.update({"phy" :x})

x = int(input("enter math :"))
marks.update({"math" : x})

x = int(input("enter chem :"))
marks.update({"chem" :x})

print(marks)

# Figure out a way to store 9 & 9.0 as separate values in the set (You can take help of built-in data types)

values = {
    ("float", 9.0),
    ("int", 9)
}
print(values)