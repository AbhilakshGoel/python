"""Astrologer Stars"""
n = int(input("How Many Rows of Stars do you want: "))
bool = bool(int(input("Enter a number 1 or 0: ")))
if bool==True:
    for i in range(0, n+1):
        print(i*"* ", end=" \n")
elif bool==False:
    for i in range(n, 0,-1):
        print(i * "* ", end=" \n")
