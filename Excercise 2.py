"""Faulty Calculator"""
print("+ for Addition, \n- for Subtraction, \n* for Multiplication, \n/ for Division" )
CalcVal = input("Which One Do You Want: ")
num1 = int(input("Enter your First Number: "))
num2 = int(input("Enter your Second Number: "))
if int(CalcVal== "+") and num1==56 and num2==9:
    print("The Sum Of Both the Numbers is 77")
elif int(CalcVal == "*") and num1 == 45 and num2 == 3:
    print("The Product Of Both the Numbers is 555")
elif int(CalcVal == "/") and num1 == 56 and num2 == 6:
    print("The Quotient Of Both the Numbers is 4")
elif int(CalcVal== "+"):
    print("The Sum Of Both the Numbers is", num1 + num2)
elif int(CalcVal=="-"):
    print("The Difference Of Both the Numbers is", num1 - num2)
elif int(CalcVal=="*"):
    print("The Product Of Both the Numbers is", num1 * num2)
elif int(CalcVal=="/"):
    print("The Quotient Of Both the Numbers is", num1 / num2)
else:
    print("Invalid Values")