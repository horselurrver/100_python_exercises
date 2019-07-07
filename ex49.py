"""
Write a function to compute 5/0 and use try/except to catch the exceptions.
"""
def divideByZero():
    try:
        x = 5/0
    except ZeroDivisionError:
        print('Cannot divide by zero')
    except Error:
        print('Caught an  exception')
    finally:
        print('Done with the block')
divideByZero()
