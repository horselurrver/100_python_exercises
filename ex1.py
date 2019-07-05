""" Write a program which will find all such numbers which are divisble by 7 but
    are not multiple of 5, between 2000 and 3200 (both included). The numbers
    obtained should be printed on a comma-separated sequence on a single line.
"""
def getNumbers():
    results = []
    for i in range(2000, 3201):
        if i % 7 == 0 and i % 5 != 0:
            results.append(str(i))
    print(', '.join(results))

if __name__ == "__main__":
    getNumbers()
