"""This Code Calculates the value of Pi with the help of Madhava's Series,
which is pi = 4/1 - 4/3 + 4/5 -4/7....4/infinity. The Limit you give is the Maximum Value of the Odd Numbers
 in the Denominator."""
def pi():
    pi = 0
    n = 4
    d = 1
    no = int(input("Enter the Limit for the Value of Pi: "))
    print("Loading... Please Wait!")
    for i in range(1,no):
        a = 2 * (i%2) - 1
        pi += a * n/d
        d += 2
    print(pi)

pi()