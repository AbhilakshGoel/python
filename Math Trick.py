"""This Code checks if the Digital Root of Every Number till the Limit given is Equal to the Digital Root
of the Number Obtained After Adding 9 to the Original Number"""

limit = int(input("Enter the Limit: "))
i = 0
while (i<=limit):
    def digital_root(n):
        if(n < 10):
            return n
        n = n%10+digital_root(n//10)
        return digital_root(n)
    i = i+1
    a = digital_root(i)
    e = digital_root(i + 9)


if (a == e):
    print("It Works!")
else:
    print("No!")


