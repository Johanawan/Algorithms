# Write a short Python function that takes a string s, representing a sentence,
# and returns a copy of the string with all punctuation removed. For example, if given the string "Let s try, Mike.", this function would return
# "Lets try Mike".

punctuation = ["'", ".", ",", "!", "?"]

def removePunc(string):
    # Turn string into list
    userInput = list(string)

    # Loop through list to find punctuation
    for i in userInput:
        if i in punctuation:
            userInput.remove(i)
        else:
            continue

    # Turn list into string
    result = "".join(userInput)
    return result


string = "Let's try Mike!"

res = removePunc(string)

print(res)