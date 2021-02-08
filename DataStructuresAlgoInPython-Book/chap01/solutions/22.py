# Write a short Python program that takes two arrays a and b of length n
# storing int values, and returns the dot product of a and b. That is, it returns
# an array c of length n such that c[i] = a[i] · b[i], for i = 0,...,n−1.

def dotProduct(a, b):

    c = []

    for i in range(len(a)):
        dotC = a[i] * b[i]
        c.append(dotC)
    return c 

a = [1, 2, 3, 4, 5, 6, 10]
b = [6, 5, 4, 3, 2, 1, 10]

res = dotProduct(a, b)

print(res)