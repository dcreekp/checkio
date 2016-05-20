"""
 In linear algebra, the transpose of a matrix A is another matrix AT (also written A′, Atr,tA or At) created by any one of the following equivalent actions:

    reflect A over its main diagonal (which runs from top-left to bottom-right) to obtain AT
    write the rows of A as the columns of AT
    write the columns of A as the rows of AT

Formally, the ith row, jth column element of AT is the jth row, ith column element of A:

[AT]i j = [A]j i

If A is an m × n matrix then AT is an n × m matrix.

You have been given a matrix as a 2D list with integers. Your task is to return a transposed matrix based on input.

transposed-matrix

Input: A matrix as a list of lists with integers.

Output: The transposed matrix as a list of lists with integers.

Example:

checkio([[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]) == [[1, 4, 7],
                         [2, 5, 8],
                         [3, 6, 9]]

checkio([[1, 4, 3],
         [8, 2, 6],
         [7, 8, 3],
         [4, 9, 6],
         [7, 8, 1]]) == [[1, 8, 7, 4, 7],
                         [4, 2, 8, 9, 8],
                         [3, 6, 3, 6, 1]]

How it is used: The most obvious use for this idea is in mathematical software, but the concept can be applied in the area of vector graphics. On a computer, one can often avoid explicitly transposing a matrix in memory by simply accessing the same data in a different order.

Precondition:
0 < len(matrix) < 10
all(0 < len(row) < 10 for row in matrix)
"""

def checkio(data):

    new = [[] for i in range(len(data[0]))]

    for n in range(len(new)):
        for d in data:
            new[n].append(d[n])

    return new


def test():

    assert checkio([[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]]) == [[1, 4, 7],
                                    [2, 5, 8],
                                    [3, 6, 9]], "Square matrix"
    assert checkio([[1, 4, 3],
                    [8, 2, 6],
                    [7, 8, 3],
                    [4, 9, 6],
                    [7, 8, 1]]) == [[1, 8, 7, 4, 7],
                                    [4, 2, 8, 9, 8],
                                    [3, 6, 3, 6, 1]], "Rectangle matrix"


def checkio_r(matr):
    'return a transposed matrix'
    return list(map(list, zip(*matr)))

def test_r():

    assert checkio_r([[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]]) == [[1, 4, 7],
                                    [2, 5, 8],
                                    [3, 6, 9]], "Square matrix"
    assert checkio_r([[1, 4, 3],
                    [8, 2, 6],
                    [7, 8, 3],
                    [4, 9, 6],
                    [7, 8, 1]]) == [[1, 8, 7, 4, 7],
                                    [4, 2, 8, 9, 8],
                                    [3, 6, 3, 6, 1]], "Rectangle matrix"



if __name__ == '__main__':

    try:
        test()
        test_r()
    except AssertionError as e:
        raise(e)
    else:
        print('all good')

