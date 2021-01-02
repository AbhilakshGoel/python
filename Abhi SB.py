import time
"""Abhi Small Basic"""
fname = input("Enter your First Name: ")
lname = input("Enter your Last Name: ")
fullname = fname + " " + lname
print("Your Fullname is", fullname)

times = input("Do you want to Show the Date And Time: ")
if times=="yes" or times=="y" or times=="Yes" or times=="YES" or times=="yo" or times=="Yo":
    localtime = time.asctime(time.localtime(time.time()))
    print(localtime)
else:
