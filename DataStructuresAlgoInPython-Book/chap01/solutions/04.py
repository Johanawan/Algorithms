# Write a short Python function that takes a positive integer n and returns
# the sum of the squares of all the positive integers smaller than n.

def sumOfSquares(x):
    # Create an empty list
    squares =[]

    # Check if x < 0
    if x <= 0:
        return "Needs to be a positive or non-zero integer."
    else:
        # take x and run a loop. 
        for i in range(1, x):
            squares.append(i**2)
        
        #print(squares)

        # Sum list squares
        return sum(squares)

res = sumOfSquares(-1)

print(res)