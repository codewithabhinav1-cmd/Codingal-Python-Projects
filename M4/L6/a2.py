import random
import time

# Pick a number between 1 and 100
number = random.randint(1, 100)

def intro():
    print("May I ask you for your name?")

    global name
    name = input()

    print(name + ", we are going to play a game. I am thinking of a number between 1 and 100")

    if number % 2 == 0:
        x = 'even'
    else:
        x = 'odd'

    print("\nThis is an {} number".format(x))

    time.sleep(0.5)
    print("Go ahead. Guess!")


def pick():
    guessesTaken = 0

    # If the number of guesses is less than 6
    while guessesTaken < 6:
        time.sleep(0.25)

        enter = input("Guess: ")

        try:
            # Convert input to integer
            guess = int(enter)

            if 1 <= guess <= 100:
                guessesTaken += 1

                if guessesTaken < 6:
                    if guess < number:
                        print("The guess of the number that you have entered is too low")

                    if guess > number:
                        print("The guess of the number that you have entered is too high")

                    if guess != number:
                        time.sleep(0.5)
                        print("Try Again!")

                # Correct guess
                if guess == number:
                    break

            else:
                print("Silly Goose! That number isn't in the range!")
                time.sleep(0.25)
                print("Please enter a number between 1 and 100")

        except:
            print("I don't think that " + enter + " is a number. Sorry")

    if guess == number:
        print("Good job, {}! You guessed my number in {} guesses!".format(name, guessesTaken))
    else:
        print("Nope. The number I was thinking of was " + str(number))


playagain = "yes"

while playagain == "yes" or playagain == "y" or playagain == "Yes":
    intro()
    pick()

    print("Do you want to play again?")
    playagain = input()