# Python allows negative integers to be used as indices into a sequence,
# such as a string. If string s has length n, and expression s[k] is used for index −n ≤ k < 0, 
# what is the equivalent index j ≥ 0 such that s[j] references the same element?

def inverseStringIndex(string):
    user_input = int(input("Give a negative integer and I'll return the position index of a string: "))
    while user_input >=0:
        if user_input > 0:
            print("You need to pick a negative number")
            user_input = int(input("Negative integer: "))
        elif user_input == 0:
            print("You need to pick a non-zero number")
            user_input = int(input("Negative integer: "))

    inverse = len(string) + user_input

    return "The index at " + str(user_input) + " is the inverse of index at " + str(inverse) + ". Which is at " + string[inverse] + "."


string = "This is a string"

res = inverseStringIndex(string)

print(res)