# Write a short Python function that takes a positive integer n and returns
# the sum of the squares of all the odd positive integers smaller than n.

def sumOddSquares(x):
    odd_squares = []

    for i in range(1, x):
        if i % 2 == 1:
            odd_squares.append(i**2)

    return sum(odd_squares)

res = sumOddSquares(18)

print(res)