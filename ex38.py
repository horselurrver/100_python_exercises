"""
Write a program which accepts a string as input to print "Yes"
if the string is "yes" or "YES" or "Yes", otherwise print "No".
"""
def printYesNo(string):
    if string.lower() == 'yes':
        print('Yes')
    else:
        print('No')
