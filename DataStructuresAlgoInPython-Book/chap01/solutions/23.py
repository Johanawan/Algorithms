# Give an example of a Python code fragment that attempts to write an element to a list based on an index that may be out of bounds. If that index
# is out of bounds, the program should catch the exception that results, and
# print the following error message:
# “Don’t try buffer overflow attacks in Python!”

def catchError(nums):
    for i in range(0, 10):
        try:
            nums[i] = 9
        except IndexError:
            return "Don't try buffer overflow attacks in Python"
    return nums

nums = [1,2,3,4,5]

res = catchError(nums)
print(res)