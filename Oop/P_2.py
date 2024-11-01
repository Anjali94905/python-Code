import random
import string
pass_len = 8
chrValues = string.ascii_letters + string.digits + string.punctuation

#list comprehension [function for i in range]
password = "".join([random.choice(chrValues)for i in range(pass_len)])

#password = ""
#for i in range(pass_len):
 #   password += random.choice(chrValues)
print("your random password is :", password)