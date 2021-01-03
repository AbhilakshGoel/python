"""Health Management System"""
def main():
    def getdate():
        import datetime
        return datetime.datetime.now()
    print("1. Harry\n2. Rohan\n3. Hamad")
    name = int(input("Whose Diet or Excercise Do you want: "))
    type = int(input("Enter 1 for Diet and 2 for Excercise: "))
    print("Do you want to Add Something or Retrieve The Data")
    log = int(input("1. Add \n2. Retrieve\nEnter your Input: "))
    if name==1 and type==1 and log==1:
        loggedtext = input("Enter your Diet for Harry: ")
        f = open("Harry Diet.txt", "a")
        date = str(getdate())
        f.write(str([date])+": "+loggedtext+"\n")
        f.close()
        print("Successfully Written")
    elif name==2 and type==1 and log==1:
        loggedtext = input("Enter your Diet for Rohan: ")
        f = open("Rohan Diet.txt", "a")
        date = str(getdate())
        f.write(str([date])+": "+loggedtext+"\n")
        f.close()
        print("Successfully Written")
    elif name==3 and type==1 and log==1:
        loggedtext = input("Enter your Diet for Hamad: ")
        f = open("Hamad Diet.txt", "a")
        date = str(getdate())
        f.write(str([date]) + ": " + loggedtext + "\n")
        f.close()
        print("Successfully Written")
    elif name==1 and type==2 and log==1:
        loggedtext = input("Enter your Excercise for Harry: ")
        f = open("Harry Excercise.txt", "a")
        date = str(getdate())
        f.write(str([date])+": "+loggedtext+"\n")
        f.close()
        print("Successfully Written")
    elif name==2 and type==2 and log==1:
        loggedtext = input("Enter your Excercise for Rohan: ")
        f = open("Rohan Excercise.txt", "a")
        date = str(getdate())
        f.write(str([date])+": "+loggedtext+"\n")
        f.close()
        print("Successfully Written")
    elif name==3 and type==2 and log==1:
        loggedtext = input("Enter your Excercise for Hamad: ")
        f = open("Hamad Excercise.txt", "a")
        date = str(getdate())
        f.write(str([date])+": "+loggedtext+"\n")
        f.close()
        print("Successfully Written")
    elif name==1 and type==1 and log==2:
        f = open("Harry Diet.txt")
        for line in f:
             print(line, end="\n")
        f.close()
    elif name==2 and type==1 and log==2:
        f = open("Rohan Diet.txt")
        for line in f:
             print(line, end="\n")
        f.close()
    elif name==3 and type==1 and log==2:
        f = open("Hamad Diet.txt")
        for line in f:
             print(line, end="\n")
        f.close()
    elif name==1 and type==2 and log==2:
        f = open("Harry Excercise.txt")
        for line in f:
             print(line, end="\n")
        f.close()
    elif name==2 and type==2 and log==2:
        f = open("Rohan Excercise.txt")
        for line in f:
             print(line, end="\n")
        f.close()
    elif name==3 and type==2 and log==2:
        f = open("Hamad Excercise.txt")
        for line in f:
            print(line, end="/n")

        f.close()
    repeat = input("Do you want to Repeat the Program y/n: ")
    if repeat=="y":
        main()
main()
