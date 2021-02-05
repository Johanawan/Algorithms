# Write a short Python function that takes a sequence of integer values and
# determines if there is a distinct pair of numbers in the sequence whose
# product is odd.

def oddProduct(nums):
  for i in range(len(nums)):
    for j in range(len(nums)):
      if  i != j:
        product = nums[i] * nums[j]
        if product % 2 == 1:
          return True
          return False

res = oddProduct([1, 2, 4, 9, 8])

print(res)

# Output - True