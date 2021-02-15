"""FIRST PROGRAM"""
# print("Hello World")

"""ESCAPE SEQUENCES"""
# print("Hello \t My Dear \n Family")
## Search For It

"""DATATYPES"""
# var01 = "Hi"
# print(type(var01))

"""STRING SLICING"""
#mytxt = "tiku is a good Boy/Girl"
#mystr = "BobbyisaGoodMom"
# print(mytxt[3])
# print(mytxt[0:4])
# print(mytxt[0:12:2])
# print(mytxt[::2])
# print(len(mytxt))
#
# print(mytxt.isalnum())
# print(mystr.isalnum())
# print(mytxt.isalpha())

# print(mytxt.endswith("Boy/Girl"))
# print(mystr.count("o"))

# print(mytxt.capitalize())
# print(mytxt.lower())
# print(mytxt.upper())

# print(mytxt.replace("tiku", "abhi"))
# print(mytxt.find("is"))

"""REVERSED ORDER OF TWO NUMBERS"""
# num1 = input("Please Enter First Number:")
# num2 = input("Please Enter Second Number:")
# num1, num2 = num2, num1
# print("The Reversed Order Respectively is" ,num1, ",", num2 )

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


