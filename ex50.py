"""
Define a custom exception class which takes a string message as attribute.
"""
class MyException(Exception):
    def __init__(self, message):
        self.message = message

error = MyException('something went wrong')
print(error.message)
