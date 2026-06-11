start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

squares = []
odd_squares = []
even_squares = []

for i in range(start, end + 1):
    sq = i ** 2
    squares.append(sq)

    if sq % 2 == 0:
        even_squares.append(sq)
    else:
        odd_squares.append(sq)

print("Square values:", squares)
print("Odd square values:", odd_squares)
print("Even square values:", even_squares)