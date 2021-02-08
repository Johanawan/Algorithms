# Write a Python program that can take a positive integer greater than 2 as
# input and write out the number of times one must repeatedly divide this
# number by 2 before getting a value less than 2.

def n2times(x):
    count = 0
    while x >=2:
        x = x/2
        count += 1
        if x<2:
            return str(count) + " times."

print(n2times(100))