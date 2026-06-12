class StringReverse:
    def __init__(self, text):
        self.__text = text   # private variable (encapsulation)

    def reverse_words(self):
        words = self.__text.split()
        reversed_string = " ".join(words[::-1])
        return reversed_string


# Taking input from user
text = input("Enter a string: ")

obj = StringReverse(text)
print("Reversed string:", obj.reverse_words())