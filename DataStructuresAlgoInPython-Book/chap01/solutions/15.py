# Write a Python function that takes a sequence of numbers and determines
# if all the numbers are different from each other (that is, they are distinct).

def uniqueValues(nums):
    x = []
    for i in nums:
        if i not in x:
            x.append(i)
    return x


res1 = uniqueValues([1, 5, 10, 15, 20])
res2 = uniqueValues([2, 5, 1, 5, 20])

print(res1)
print(res2)