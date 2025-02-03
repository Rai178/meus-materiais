# [expression for item in iterable]
squares = [x**2 for x in range(10)]
print(squares) # output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

#filtering:
even_numbers = [x for x in range(10) if x % 2 == 0]

#mapping:
squares = [x**2 for x in range(10)]

#combining filtering and mapping:
even_squares = [x**2 for x in range(10) if x % 2 == 0]

#nested loops:
matrix = [[j for j in range(3)] for i in range(2)]
