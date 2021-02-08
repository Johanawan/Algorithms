# Had we implemented the scale function (page 25) as follows, does it work
# properly?
# def scale(data, factor):
#   for val in data:
#       val *= factor
# Explain why or why not.

def wrongScale(data, factor):
    for val in data:
        val *= factor
    return data

def rightScale(data, factor):
    for val in range(len(data)):
        data[val] *= factor
    return data

res = rightScale([1,2,3,4,5,6,7,8,9,10], 10)

print(res)

"""
val *= factor creates a new instance of val, and does not change the original object (data).
If you want to change a list you need to use data[val] *= factor. This mutates the current object.
"""