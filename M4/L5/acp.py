# 1. Create lists of odd and even numbers below the input number

n = int(input("Enter a number: "))

odd_numbers = [i for i in range(n) if i % 2 != 0]
even_numbers = [i for i in range(n) if i % 2 == 0]

print("Odd Numbers:", odd_numbers)
print("Even Numbers:", even_numbers)


# 2. Create a list of fruits and capitalize each element

fruits = ["apple", "banana", "mango", "orange", "grapes"]

updated_fruits = [fruit.capitalize() for fruit in fruits]

print("Original List:", fruits)
print("Updated List:", updated_fruits)