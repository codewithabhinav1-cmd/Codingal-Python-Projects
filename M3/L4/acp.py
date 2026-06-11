try:
    age = int(input("Enter your age: "))

    if age < 0:
        print("Invalid age")
    elif age % 2 == 0:
        print("Age is Even")
    else:
        print("Age is Odd")

except ValueError:
    print("Please enter a valid age")