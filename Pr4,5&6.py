# Hello!
print("This is a program for finding sqaure root")
num=int(input("Please enter the number:"))
sqroot=num**0.5
print("The sqaure root of your given number,",num,"is",sqroot)
ro=sqroot//1
print("The rounded-off version of that root is",int(ro))
# Okay, this works.

"""num2=int(input("Enter another number for cube root:"))
curoot=num2**0.25
print(curoot)"""
# Ma'am this is not working!!!

"""Upper is Pr4, lower is Pr5"""

# Project 23/11/24 C5
# Since divisibility rule of 6 is that the given number should be even and divisible by 3, we'll do it that way.
print("This is a program to check if a number is divisible by 6!")
num=int(input("Enter a number to see if it is divisible by 6:"))
a=num%2
if a==0 :
    b=True
else:
    b=False

a2=num%3

if a2==0:
    c=True
else:
    c=False

if b==True and c==True:
    print("Your number is divisible by 6!!!")
else:
    print("Your number is not divisible by 6...")    

# Thank you mam!


"""Upper is Pr5, lower is Pr6"""

# Project for senior citizen discount.
age=int(input("Enter you age:"))
if age>=60:
    print("You are eligible for senior citizen discount.")
else:
    print("You are not eligible for senior citizen discount, yet.")

# Project for leap year
cy=int(input("Enter the current year:"))
ystr=str(cy)
if ystr.endswith("00"):
    if cy%400==0:
        print("This year is a leap year.")
    else:
        print("This year is not a leap year.")
else:
    if cy%4==0:
        print("This year is a leap year.")
    else:
        print("This year is not a leap year.")

# Does it work?
# Yes it does!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!