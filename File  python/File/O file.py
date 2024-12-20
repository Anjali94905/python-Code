# (Q1) Create a new file "practice.txt" using python . Add the following data in it:
with open("practice.txt","w")as f :
     f.write("Hi everyone\nwe are learning File I/O \N")
     f.write("using Java .\nI like programming in Java.")
     
# (Q2) WPA that replace all occurrences of "Java" with "python"in above file.
with open("practice.txt","r")as f:
    data = f.read()

new_data = data.replace( "Java","Python")
print(new_data)

with open("practice.txt","w")as f:
    f.write(new_data)


# (Q3) Search if the word "learning" exist in the file or not.
def check_for_word():
    word = "xlearning"
    with open("practice.txt","r")as f :
          data = f.read()
    if data.find(word) !=-1 :
        print("found")
    else:
        print("not found")

check_for_word()

# (Q3) WAP to find in which line of the file does the word "learning" occur first.Print -1 if word not found.

def check_for_line():
    word = "learning"
    data = True
    line_no = 1
    with open("practice.txt","r")as f:
        while data:
            data = f.readline()
            if word in data :
                print(line_no)
                return
            line_no += 1
    return -1
print(check_for_line())

 #(Q4) From a file containing numbers separated by comma, print the count os even numbers.
count = 0
with open("practice.txt","r")as f:
    data = f.read()

    nums = data.split(",")
    for val in nums:
       if int(val)% 2 == 0 :
          count += 1

print(count)
with open("practice.txt","w")as f:         
 f.close()

