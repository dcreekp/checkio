"""
 Tic-Tac-Toe, sometimes also known as Xs and Os, is a game for two players (X and O) who take turns marking the spaces in a 3×3 grid. The player who succeeds in placing three respective marks in a horizontal, vertical, or diagonal rows (NW-SE and NE-SW) wins the game.

But we will not be playing this game. You will be the referee for this games results. You are given a result of a game and you must determine if the game ends in a win or a draw as well as who will be the winner. Make sure to return "X" if the X-player wins and "O" if the O-player wins. If the game is a draw, return "D".
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
"""

def checkio(game_result):

    lines = [game_result[n] for n in range(3)]

    lines2 = [[game_result[m][n] for m in range(3)] for n in range(3)]

    lines.append(game_result[0][0] + game_result[1][1] + game_result[2][2])
    lines.append(game_result[0][2] + game_result[1][1] + game_result[2][0])

    lines2 = [''.join(line) for line in lines2]

    lines = lines + lines2

    print(lines)
    for line in lines:
        if line == 'XXX':
            return 'X'
        if line == 'OOO':
            return 'O'
    else:
        return 'D'


def test():

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

    try:
        test()
    except AssertionError as e:
        raise(e)
    else:
        print('all good')
