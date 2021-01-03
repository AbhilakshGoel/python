"""Snake, Water, Gun Game"""
import random
win = 0
tie = 0
lose = 0
repeats = 0
round = 1
options = ["Snake", "Water", "Gun"]
print("This is Snake, Water and Gun Game")
print("You have 10 Rounds")
print("s for Snake\nw for Water\ng for Gun")
while(repeats<10):
    print("Round", round)
    computer = random.choice(options)
    user = input("Enter your Option: ")
    print('\n')

    if user=="g" and computer=="Gun":
        print(f"Computer's Choice: {computer}")
        print("Your Choice: Gun")
        print(f"The Computer also Chose the Same as you")
        print("Tie!\n")
        repeats = repeats+1
        tie = tie+1
    elif user=="w" and computer=="Water":
        print(f"Computer's Choice: {computer}")
        print("Your Choice: Water")
        print(f"The Computer also Chose the Same as you")
        print("Tie!\n")
        repeats = repeats+1
        tie = tie+1
    elif user=="s" and computer=="Snake":
        print(f"Computer's Choice: {computer}")
        print("Your Choice: Snake")
        print(f"The Computer also Chose the Same as you")
        print("Tie!\n")
        repeats = repeats+1
        tie = tie+1
    elif user=="s" and computer=="Water":
        print(f"Computer's Choice: {computer}")
        print(f"Your Choice: Snake")
        print("You Won!\n")
        repeats = repeats+1
        win = win+1
    elif user=="s" and computer=="Gun":
        print(f"Computer's Choice: {computer}")
        print("Your Choice: Snake")
        print("The Computer Won!\n")
        repeats = repeats+1
        lose = lose+1
    elif user=="w" and computer=="Snake":
        print(f"Computer's Choice: {computer}")
        print("Your Choice: Water")
        print("The Computer Won!\n")
        repeats = repeats+1
        lose = lose+1
    elif user=="w" and computer=="Gun":
        print(f"Computer's Choice: {computer}")
        print("Your Choice: Water")
        print("You Won!\n")
        repeats = repeats+1
        win = win+1
    elif user=="g" and computer=="Snake":
        print(f"Computer's Choice: {computer}")
        print("Your Choice: Gun")
        print("You Won!\n")
        repeats = repeats + 1
        win = win + 1
    elif user=="g" and computer=="Water":
        print(f"Computer's Choice: {computer}")
        print("Your Choice: Gun")
        print("The Computer Won!\n")
        repeats = repeats + 1
        lose = lose+1
    round = round + 1
print(f"Wins: {win}\nLoses: {lose}\nTie: {tie}")
print("Thanks for Playing!")






