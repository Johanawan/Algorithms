# Write a short Python function, is even(k), that takes an integer value and
# returns True if k is even, and False otherwise. However, your function
# cannot use the multiplication, modulo, or division operators.

def is_even(k):
    if k <= 0:
        return -1
    else:
        # Method 1: Using modulus
        # if k % 2 ==0:
        #     return True
        # else:
        #     return False

        # Method 2: Loops
        isEven = True
        for i in range(1, k+1):
            if isEven == True:
                isEven = False
            else:
                isEven = True
        
        if isEven == True:
            return True
        else:
            return False

res = is_even(10)

print(res)