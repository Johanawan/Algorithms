# Write a short Python function that counts the number of vowels in a given
# character string.

vowels_list = ["a", "e", "i", "o", "u"]

def vowelsCount(string):
    vowels = 0
    for i in string:
        if i in vowels_list:
            vowels += 1
        else:
            continue
    return vowels

userInput = input("What would you like to say?\n")

res = vowelsCount(userInput)

print(res)