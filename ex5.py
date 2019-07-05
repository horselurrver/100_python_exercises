"""
    Define a class which has at least two methods: getString to get a string from console
    input and printString to string the string in upper case.
"""

class StringClass:
    def __init__(self):
        self.string = ''

    def getString(self):
        self.string = input('Please enter a string ')

    def printString(self):
        print(self.string.upper())

instance = StringClass()
instance.getString()
instance.printString()
