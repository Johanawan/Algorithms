# Give a single command that computes the sum from 06.py, 
# relying on Python’s comprehension syntax and the built-in sum function.

def sumOddSquares(x):
    result = sum([i**2 for i in range(1, x) if i % 2 == 1])
    return result

res = sumOddSquares(18)

print(res)