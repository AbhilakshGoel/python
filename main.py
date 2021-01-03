"""FIRST PROGRAM"""
# print("Hello World")
print("You are Great!")

# """SUM OF TWO NUMBERS"""
# num1 = input("Please Enter First Number:")
# num2 = input("Please Enter Second Number:")
# print("The Sum of Both the Numbers is", int(num1) + int(num2))

"""REVERSED ORDER OF TWO NUMBERS"""
# num1 = input("Please Enter First Number:")
# num2 = input("Please Enter Second Number:")
# num1, num2 = num2, num1
# print("The Reversed Order Respectively is" ,num1, ",", num2 )

"""Age"""
# age = input("What Is Your Age:")
# if int(age)<18:
#     print("Leagally, You are not Allowed to Vote")
# elif int(age)==18:
#     print("We will Think about You")
# else:
#     print("You are Allowed to Vote")

"""Quiz Practice"""
# list = ["Mommy", 3, "Tommy", 4, "Bobby", float, 6, 10, 50, 230, 500, 1000]
# for item in list:
#     if str(item).isnumeric() and item>6:
#         print(item)

"""Percentage Calculator"""
# print("Enter Your Total Marks: ")
# tmarks = int(input())
# print("Enter the Maximum Marks: ")
# maxmarks = int(input())
# print("Your Percentage is", tmarks/maxmarks*100, "%")

"""Tables"""
# table = int(input("Which Table do You Want to Learn: "))
# print(table, "* 1 =", table*1)
# print(table, "* 2 =", table*2)
# print(table, "* 3 =", table*3)
# print(table, "* 4 =", table*4)
# print(table, "* 5 =", table*5)
# print(table, "* 6 =", table*6)
# print(table, "* 7 =", table*7)
# print(table, "* 8 =", table*8)
# print(table, "* 9 =", table*9)
# print(table, "* 10 =", table*10)

"""While Loop Quiz"""
# while(True):
#     val = int(input("Enter your Number: "))
#     if val<=100:
#         print("Try Again !")
#         continue
#     elif val>100:
#         print("You Successfully Entered a Number Greater than 100")
#         break

"""try-except Error Handling"""
# try:
#     num1 = input("Please Enter First Number:")
#     num2 = input("Please Enter Second Number:")
#     print("The Sum of Both the Numbers is", int(num1) + int(num2))
#
# except Exception as e:
#     print(e)

# n! = n * n-1 * n-2 * n-3.......1
# n! = n * (n-1)!

"""Iterative Factorial"""
# def factorial_iterative(n):
#     """
#         :param n: Integer
#         :return: n * n-1 * n-2 * n-3.......1
#     """
#     fac = 1
#     for i in range(n):
#         fac = fac * (i + 1)
#     return fac
#
"""Recursive Factorial"""
# def factorial_recursive(n):
#     """
#         :param n: Integer
#         :return: n * n-1 * n-2 * n-3.......1
#     """
#     if n == 1:
#         return 1
#     else:
#         return n * factorial_recursive(n - 1)
#     # 5 * factorial_recursive(4)
#     # 5 * 4 * factorial_recursive(3)
#     # 5 * 4 * 3 * factorial_recursive(2)
#     # 5 * 4 * 3 * 2 * factorial_recursive(1)
#     # 5 * 4 * 3 * 2 * 1 = 120
#
#
#
# number = int(input("Enter then number"))
# # print("Factorial Using Iterative Method", factorial_iterative(number))
# # print("Factorial Using Recursive Method", factorial_recursive(number))
#

"""Fibonacci Sequence"""
# def fibonacci1(n):
#     if n==1 or n==0:
#         ans = f"0 is the Fibonacci Number at {n}'s place"
#         return 0
#     elif n==2:
#         ans = "1 is the Fibonacci Number at 2nd place"
#         return 1
#     else:
#         ans = fibonacci1(n-1)+ fibonacci1(n-2)
#         return ans
# number = int(input("Which Fibonacci Number Do you Want: "))
# print(fibonacci1(number))

## 0 1 1 2 3 5 8 13 21
