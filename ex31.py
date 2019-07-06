"""
Define a function that can accept two strings as input and print the string with maximum length
in console. If two strings have the same length, then the function should print all strings line by line.
"""
def maxLen(string1, string2):
    if len(string1) == len(string2):
        print(string1)
        print(string2)
    elif len(string1) > len(string2):
        print(string1)
    else:
        print(string2)
