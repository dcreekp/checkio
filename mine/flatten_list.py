'''
 There is a list which contains integers or other nested lists which may contain yet more lists and integers which then… you get the idea. You should put all of the integer values into one flat list. The order should be as it was in the original list with string representation from left to right.

We need to hide this program from Nikola by keeping it small and easy to hide. Because of this, your code should be shorter than 140 characters (with whitespaces).

Input data: A nested list with integers.

Output data: The one-dimensional list with integers.

Example:

flat_list([1, 2, 3]) == [1, 2, 3]
flat_list([1, [2, 2, 2], 4]) == [1, 2, 2, 2, 4]
flat_list([[[2]], [4, [5, 6, [6], 6, 6, 6], 7]]) == [2, 4, 5, 6, 6, 6, 6, 6, 7]
flat_list([-1, [1, [-2], 1], -1]) == [-1, 1, -2, 1, -1]

How it is used: This concept is useful for parsing and analyzing files with complex structures and the task challenges your creativity in writing short code.

Precondition: 0 ≤ |array| ≤ 100
∀ x ∈ array : -232 < x < 232 or x is a list
depth < 10
'''

def flat_list(lst):

    def flatten(lst, new_lst, hold=None):
        if not lst and not hold:
            return new_lst[::-1]
        if hold and not lst:
            lst = hold
        item = lst.pop()
        if type(item) is int:
            new_lst.append(item)
            return  flatten(lst, new_lst, hold)
        else:
            hold = hold + lst if hold else lst
            return flatten(item, new_lst, hold)

    return flatten(lst, [])

"""
def flat_listx(lst):
    import itertools as it
    import functools as f

    def flat(x, y):
        while type(x) is list:
            pass
        if type(x) is list and type(y) is list:
            return x + y
        else:
            return y
    return f.reduce(lambda x,y: x + y, lst, [lst[0]])

    def flatten(lst):
        r = []
        for i in lst:
            while type(i) is list and i != None:
                if type(i.pop()) == int:
                    r.append(i.pop())
"""



def test_flat_list():

    assert flat_list([1, 2, 3]) == [1, 2, 3]
    assert flat_list([1, [2, 2, 2], 4]) == [1, 2, 2, 2, 4]
    assert flat_list([[[2]], [4, [5, 6, [6], 6, 6, 6], 7]]) == [2, 4, 5, 6, 6, 6, 6, 6, 7]
    assert flat_list([-1, [1, [-2], 1], -1]) == [-1, 1, -2, 1, -1]

if __name__ == "__main__":

    test_flat_list()
