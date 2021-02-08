# Demonstrate how to use Python’s list comprehension syntax to produce
# the list [ a , b , c , ..., z ], but without having to type all 26 such
# characters literally.

def alphabet():
    res = [chr(97 + x) for x in range(26)]
    return res

res = alphabet()
print(res)