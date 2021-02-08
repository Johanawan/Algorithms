# A common punishment for school children is to write out a sentence multiple times. Write a Python stand-alone program that will write out the
# following sentence one hundred times: “I will never spam my friends
# again.” Your program should number each of the sentences and it should
# make eight different random-looking typos.

import random


def create_typo(message, char_range):
    error_spot = random.randrange(0, len(message))
    error_character = random.choice(char_range)
    incorrect_message = list(message)
    incorrect_message[error_spot] = chr(error_character)
    return (''.join(incorrect_message))
    



def spamalot(message, num_errors = 8, num_lines = 100):
    #find all the character values for Aa-Zz
    char_range = list(range(ord('A'), ord('Z')+1)) + list(range(ord('a'), ord('z')+1))
    message
    
    line_count = 0
    error_lines = set()
    while line_count <num_errors:
        new_error_line = random.randrange(num_lines)
        if new_error_line not in error_lines:
            error_lines.add(new_error_line)
            line_count += 1
    
    for i in range (num_lines):
        if i not in error_lines:
            print (message)
        else:
            print (create_typo(message, char_range), '<- This is the typo')
            
            
spamalot('I will never spam my friends again')