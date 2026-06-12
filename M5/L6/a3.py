import random

class FruitQuiz:
    # Constructor
    def __init__(self):
        # Dictionary of fruits and their colors
        self.fruits = {
            "apple": "red",
            "orange": "orange",
            "watermelon": "green",
            "banana": "yellow"
        }

    # Quiz function
    def quiz(self):
        while True:
            fruit, color = random.choice(list(self.fruits.items()))

            print("What is the color of {}?".format(fruit))
            user_answer = input("Your answer: ")

            if user_answer.lower() == color:
                print("Correct answer!")
            else:
                print("Wrong answer!")

            option = int(input("Enter 0 to play again, otherwise enter 1: "))

            if option:
                break


print("Welcome to Fruit Quiz")

fq = FruitQuiz()
fq.quiz()