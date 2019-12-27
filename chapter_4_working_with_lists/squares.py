digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(f"{min(digits)}")
print(f"{max(digits)}")
print(f"{sum(digits)}")


# define empty list
squares = []
# define range of numbers that we will multiple with itselfs
for value in range(1, 11):
    square = value ** 2
    squares.append(square)
print(squares)

# we have  few ways how we can multiple numbers with itself and add it to our empty list
squares = []
for value in range(1, 11):
    squares.append(value ** 2)
print(squares)

# put all this in one line
squares = [value**2 for value in range(1, 11)]
print(squares)

