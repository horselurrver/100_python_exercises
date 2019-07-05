"""
    Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array.
    The element value in the i-th row and j-th column of the array should be i*j.
    Note: i=0,1.., X-1; j=0,1,¡­Y-1.
"""
def generateArray(row, col):
    result = []
    for i in range(row):
        rowArray = []
        for j in range(col):
            rowArray.append(i * j)
        result.append(rowArray)
    print(result)

generateArray(3, 5)
