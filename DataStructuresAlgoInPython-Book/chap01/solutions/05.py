# Give a single command that computes the sum from  04.py, 
# relying on Python’s comprehension syntax and the built-in sum function.

def sumOfSquares(x):
    result = sum([x**2 for x in range(x)])
    return result

res = sumOfSquares(4)

print(res)