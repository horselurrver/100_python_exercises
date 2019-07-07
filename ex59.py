"""
The Fibonacci Sequence is computed based on the following formula:

f(n)=0 if n=0
f(n)=1 if n=1
f(n)=f(n-1)+f(n-2) if n>1

Please write a program to compute the value of f(n) with a given n input by console.

Example:
If the following n is given as input to the program:

7

Then, the output of the program should be:

13

In case of input data being supplied to the question, it should be assumed to be a console input.
"""
def fibonnaci(num):
    if num == 0 or num == 1:
        return num
    return fibonnaci(num - 1) + fibonnaci(num - 2)

if __name__ == "__main__":
    print(fibonnaci(7))
