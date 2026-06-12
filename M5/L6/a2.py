class Flashcard:
    def __init__(self, word, meaning):
        self.word = word
        self.meaning = meaning

    def __str__(self):
        # Return a string representation of the flashcard
        return self.word + " ( " + self.meaning + " )"


flash = []

print("Welcome to Flashcard Application")

# Repeat until the user chooses to stop
while True:
    word = input("Enter the word you want to add to flashcard: ")
    meaning = input("Enter the meaning of the word: ")

    flash.append(Flashcard(word, meaning))

    option = int(input("Enter 0 to add another flashcard, otherwise enter 1: "))

    if option:
        break

# Print all flashcards
print("\nYour Flashcards")

for i in flash:
    print(">", i)