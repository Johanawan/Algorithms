# Write a Python program that outputs all possible strings formed by using
# the characters c , a , t , d , o , and g exactly once.

from itertools import permutations

perms = ["".join(p) for p in permutations("catdog")]

print(perms)