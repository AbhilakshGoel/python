"""Guess The Number"""
guess = 1
n = 18
lives = 9
print("This is a Number Guessing Game")
print("There are only 9 Guesses")
userguess = int(input("Guess a number between 1 and 50: "))
while(userguess<=50):
    if guess<lives:

        if userguess<n:
            # print("Enter a Bigger Number and Try Again")
            guess = guess + 1
            userguess = int(input("Enter a Bigger Number and Try Again: "))
            while (guess >= 5):
                print(lives - guess, "Guesses Left")
                break
        elif userguess>n:
            # print("Enter a Smaller Number and Try Again")
            guess = guess + 1
            userguess = int(input("Enter a Smaller Number and Try Again: "))
            while (guess >= 5):
                print(lives - guess, "Guesses Left")
                break

        elif userguess==n:
            print("You Successfully Guessed The Correct Number that was", n)
            print("You took", guess, "Guesses to Finish")
            break
        # else guess>=6:
        #     print(lives-guess, "Guesses Left")
        #     continue
    else:
        print("Your Guesses Are Over")
        print("Game Over!")
        break
else:
    print("Invalid Input")
