# Demonstrate how to use Python’s list comprehension syntax to produce
# the list [0, 2, 6, 12, 20, 30, 42, 56, 72, 90].

def sequence():
    res = [x* (x + 1) for x in range(10)]
    return res

res = sequence()
print(res)