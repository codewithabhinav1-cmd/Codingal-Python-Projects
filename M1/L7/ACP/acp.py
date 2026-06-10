char = input("Enter a character: ")

alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

if char in alphabets:
    print(char, "is an alphabet.")
    print("ASCII Value =", ord(char))
else:
    print(char, "is not an alphabet.")