# Write a short program that takes as input three integers, a, b, and c, from
# the console and determines if they can be used in a correct arithmetic
# formula (in the given order), like “a+b = c,” “a = b−c,” or “a ∗ b = c.”

import operator

def boolArithmetic(a, b, c):

    operator_list = [operator.add, operator.sub, 
                     operator.mul, operator.truediv] 
    result_list = [] 
    for op in operator_list: 
        if a == op(float(b),float(c)): 
            result_list.append(op.__name__) 
        if c == op(float(a),float(b)): 
            result_list.append(op.__name__) 
    return result_list

a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

res = boolArithmetic(a, b, c)

print(res)