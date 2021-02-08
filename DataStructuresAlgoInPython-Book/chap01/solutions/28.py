import math

def p_norm(v, p=2):
    assert p!=0, 'p-value cannot be 0'
    sum = 0
    for num in v:
        sum += num**p
    return sum**(1/p)
    
print(p_norm([4,3]))
print(p_norm([4,3, 4, 5], 3))