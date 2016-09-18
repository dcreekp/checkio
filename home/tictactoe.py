'''
 A game's result is presented as a list of strings, where "X" and "O" are players' marks and "." is the empty cell.

Input: A game result as a list of strings (unicode).

Output: "X", "O" or "D" as a string.

Example:

checkio([
    "X.O",
    "XX.",
    "XOO"]) == "X"
checkio([
    "OO.",
    "XOX",
    "XOX"]) == "O"
checkio([
    "OOX",
    "XXO",
    "OXX"]) == "D"

How it is used: The concepts in this task will help you when iterating data types. They can also be used in game algorithms, allowing you to know how to check results.

Precondition:
There is either one winner or a draw.
len(game_result) == 3
all(len(row) == 3 for row in game_result)
'''


def checkio(game_result):

    N = 3

    rows = [[c for c in row] for row in game_result]
    d1 = [[rows[i][i] for i in range(N)]]
    d2 = [[rows[N - 1 - i][i] for i in range(N)]]
    cols = list(zip(*game_result))

    result = rows + d1 + d2 + cols

    for lst in result:
        if len(set(lst)) == 1 and lst[0] != '.':
            return lst[0]
    return "D"

def test_checkio():
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"

if __name__ == '__main__':
    test_checkio()
