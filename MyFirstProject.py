print("WELCOME TO XYZ STORE")
username = input("Please Enter your Name: ")
print("Welcome", username, "to Our Store")
print("What Do You Want ?")
print("1. Clothes")
print("2. Medicines")
print("3. Groceries")
print("4. Toys")
print("5. Games")
choice = int(input("Enter Your Choice[1-5]: "))

if choice==1:
    print("Welcome To The Clothes Store")
    print("What Do you Want To Buy ?")
    print("1. T-Shirt")
elif choice==2:
    print("Welcome To The Medicines Store")
elif choice==3:
    print("Welcome To The Grocery Store")
elif choice==4:
    print("Welcome To Toy Store")
elif choice==5:
    print("Welcome To The Games Store")
else:
    print("Invalid Choice")
