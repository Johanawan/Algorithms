# Write a short Python function, is_multiple(n, m), that takes two integer
# values and returns True if n is a multiple of m, that is, n = mi for some
# integer i, and False otherwise.

def is_multiple(n, m):
    if n <= 0 or m <= 0:
        return -1
    else:
        if m % n == 0:
            return True
        else:
            return False

res = is_multiple(6,12)

print(res)