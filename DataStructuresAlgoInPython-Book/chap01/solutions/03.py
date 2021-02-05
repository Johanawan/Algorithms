# Write a short Python function, minmax(data), that takes a sequence of
# one or more numbers, and returns the smallest and largest numbers, in the
# form of a tuple of length two. Do not use the built-in functions min or
# max in implementing your solution.

def minmax(data):
    if len(data) <= 0:
        return -1
    else:
        min_number = max_number = data[0]
        for i in data[1:]:
            if i < min_number:
                min_number = i
            else:
                if i > max_number:
                    max_number = i

        return (min_number, max_number)

numbers= [63,31,3,199,70,20]

res = minmax(numbers)

print(res)