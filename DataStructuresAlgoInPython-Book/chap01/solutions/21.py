# Write a Python program that repeatedly reads lines from standard input
# until an EOFError is raised, and then outputs those lines in reverse order
# (a user can indicate end of input by typing ctrl-D).

done = False
lines = []

# Not working

# while not done:
#     try:
#         line = input('Enter text, i shall print it in reversed order, ctrl-d to stop')
#         lines.append(line)
#     except (EOFError):
#         for l in range(len(lines) - 1, -1, -1):
#             print(lines[l])
#             done = True