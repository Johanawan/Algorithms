# Write a function that reverses a list of n
# integers, so that the numbers are listed in the opposite order than they
# were before, and compare this method to an equivalent Python function
# for doing the same thing.

def reverselist(numbers):
    newList = []
    while numbers:
        newList.append(numbers.pop())

    return newList

res = reverselist([1, 11, 21, 31, 41, 51, 61, 71])

print(res)