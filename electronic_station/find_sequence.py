"""
You are given a matrix of NxN (4≤N≤10). You should check if there is a sequence of 4 or more matching digits. The sequence may be positioned horizontally, vertically or diagonally (NW-SE or NE-SW diagonals).

Input: A matrix as a list of lists with integers.

Output: Whether or not a sequence exists as a boolean.

Example:

checkio([

    [1, 2, 1, 1],

    [1, 1, 4, 1],

    [1, 3, 1, 6],

    [1, 7, 2, 5]

]) == True

checkio([

    [7, 1, 4, 1],

    [1, 2, 5, 2],

    [3, 4, 1, 3],

    [1, 1, 8, 1]

]) == False

checkio([

    [2, 1, 1, 6, 1],

    [1, 3, 2, 1, 1],

    [4, 1, 1, 3, 1],

    [5, 5, 5, 5, 5],

    [1, 1, 3, 1, 1]

]) == True

checkio([

    [7, 1, 1, 8, 1, 1],

    [1, 1, 7, 3, 1, 5],

    [2, 3, 1, 2, 5, 1],

    [1, 1, 1, 5, 1, 4],

    [4, 6, 5, 1, 3, 1],

    [1, 1, 9, 1, 2, 1]

    ]) == True


How it is used: This concept is useful for games where you need to detect various lines of the same elements (match 3 games for example). This algorithm can be used for basic pattern recognition.

Precondition:
0 ≤ len(matrix) ≤ 10
all(all(0 < x < 10 for x in row) for row in matrix)
"""

def checkio1(matrix):
    match = False

    # create dictionary of key as number value as list of coordinates
    val2coord = {}
    for y,  row in enumerate(matrix):
        for x, val in enumerate(row):
             val2coord[val] = val2coord.get(val, [])
             val2coord[val].append((x,y))

    for key, lst in val2coord.items():
        if len(lst) < 4:
            pass

    print(val2coord[3])


    return match

def checkio(matrix):

    def row_count(matrix):
        for row in matrix:
            count, value = 0, 0
            for check in row:
                if check == value:
                    count += 1
                else:
                    value = check
                    count = 1
                if count >= 4:
                    return True
        return False

    if row_count(matrix):
        return True

    transpose_matrix = list(zip(*matrix))

    if row_count(transpose_matrix):
        return True

    def diagonals(matrix):
        diagonals = []
        N = len(matrix)
        for i in range(N - 3):
            xx = [matrix[i+r][r] for r in range(N - i)]
            yy = [matrix[r][i+r] for r in range(N - i)]
            diagonals.append(yy)
            diagonals.append(xx)
        return diagonals

    if row_count(diagonals(matrix)):
        return True

    reverse_matrix = [ row[::-1] for row in matrix]

    if row_count(diagonals(reverse_matrix)):
         return True

    return False

def checkio2(matrix):

    def diagonals(sample):
        diagonals = []
        h, w = len(sample), len(sample[0])
        for p in range(h + w - 1):
            for q in range(min(p, h - 1), max(0, p - w + 1) -1, -1):
                diagonals.append(sample[h - 1 - q][p - q])
        return diagonals

    def four_in_row(sample):
        for row in sample:
            s = ''.join(str(x) for x in row)
            for n in row:
                if str(n) * 4 in s:
                    return True
        return False





def test_checkio():

    assert checkio([
        [1, 2, 1, 1],
        [1, 1, 4, 1],
        [1, 3, 1, 6],
        [1, 7, 2, 5]
    ]) == True, "Vertical"
    assert checkio([
        [7, 1, 4, 1],
        [1, 2, 5, 2],
        [3, 4, 1, 3],
        [1, 1, 8, 1]
    ]) == False, "Nothing here"
    assert checkio([
        [2, 1, 1, 6, 1],
        [1, 3, 2, 1, 1],
        [4, 1, 1, 3, 1],
        [5, 5, 5, 5, 5],
        [1, 1, 3, 1, 1]
    ]) == True, "Long Horizontal"
    assert checkio([
        [7, 1, 1, 8, 1, 1],
        [1, 1, 7, 3, 1, 5],
        [2, 3, 1, 2, 5, 1],
        [1, 1, 1, 5, 1, 4],
        [4, 6, 5, 1, 3, 1],
        [1, 1, 9, 1, 2, 1]
    ]) == True, "Diagonal"


if __name__ == '__main__':
    test_checkio()



