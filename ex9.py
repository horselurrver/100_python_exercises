"""
    Write a program that accepts sequence of lines as input and prints the lines
    after making all characters in the sentence capitalized.
    Suppose the following input is supplied to the program:
    Hello world
    Practice makes perfect
    Then, the output should be:
    HELLO WORLD
    PRACTICE MAKES PERFECT
"""
def capitalize():
    result = ''
    while True:
        line = input()
        if line:
            result = result + line.upper() + '\n'
        else:
            break
    print(result)

capitalize()
