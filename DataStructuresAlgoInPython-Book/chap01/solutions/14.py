# Write a short Python function that takes a sequence of integer values and
# determines if there is a distinct pair of numbers in the sequence whose
# product is odd.

def oddProduct(nums):
  odd_count = 0
  for i in nums:
    if i % 2 == 0:
      continue
    else:
      odd_count += 1
  
  if odd_count >= 2:
    return True
  else:
    return False

res1 = oddProduct([1, 2, 4, 9, 8])
res2 = oddProduct([1, 1, 4, 10, 8])

print(res1)
print(res2)

# Output - True, False