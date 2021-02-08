# Write a Python program that can “make change.” Your program should
# take two numbers as input, one that is a monetary amount charged and the
# other that is a monetary amount given. It should then return the number
# of each kind of bill and coin to give back as change for the difference
# between the amount given and the amount charged. The values assigned
# to the bills and coins can be based on the monetary system of any current
# or former government. Try to design your program so that it returns as
# few bills and coins as possible.

def getChange(given, charged, denominations= [100, 20, 10, 5, 1, 0.50, 0.20, 0.10, 0.05, 0.02, 0.01]):
    assert given >= charged
    change = {}
    residual = given - charged
    for denomination in denominations:
        amount, residual = divmod(residual, denomination)
        if amount: change[denomination] = int(amount) #This will only add non-zero amounts to the dictionary
    return change

print(getChange(1000, 575))
print(getChange(1232.91, 290.66))