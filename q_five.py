
# (Q1) WAP to print the length of a list.
'''cities = ["delhi", "gurgaon", "noida", "pune","mumbai", "chennai"]
heroes = ["thor", "ironman", "captain america", "shaktiman"]

def print_len(list):
    print(len(list))

print_len(cities)
print_len(heroes)'''

# (Q2) WAP to print the element of a list in a single line.
'''cities = ["delhi", "gurgaon", "noida", "pune","mumbai", "chennai"]
heroes = ["thor", "ironman", "captain america", "shaktiman"]

def print_len(list):
    print(len(list))

def print_list(list):
    for item in list:
        print(item , end=" ")

print_list(cities)
print_list(heroes)
print()'''

#(Q3) WAF to find the factorial of n.
'''def cal_fact(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    print(fact)

cal_fact(3)'''

# (Q4) WAF to convert USD to INR. 
def converter(usd_val):
    inr_val = usd_val * 83
    print(usd_val,"USD=",inr_val,"INR")

converter(1)