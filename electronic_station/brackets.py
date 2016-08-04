"""

“Great!” Exclaimed Sofia. “Now we have the password.”

“To what exactly?” Quipped Nikola.

“Untold treasures, vast riches beyond belief! Gold! Silver! Silicon! Hydraulic Fluid! Anything your heart desires!”

“And you’re going to do what with a password to absolutely nothing?” Nikola smirked.

“Oh... Right...”

Stephen spoke up. “Well, this door back here has a keypad. Only thing is the brackets look pretty busted up. We could try fixing it and then punching in the password?”

“YES! That!” Sofia exclaimed.

You are given an expression with numbers, brackets and operators. For this task only the brackets matter. Brackets come in three flavors: "{}" "()" or "[]". Brackets are used to determine scope or to restrict some expression. If a bracket is open, then it must be closed with a closing bracket of the same type. The scope of a bracket must not intersected by another bracket. In this task you should make a decision, whether to correct an expression or not based on the brackets. Do not worry about operators and operands.

Input: An expression with different of types brackets as a string (unicode).

Output: A verdict on the correctness of the expression in boolean (True or False).

Example:

checkio("((5+3)*2+1)") == True

checkio("{[(3+1)+2]+}") == True

checkio("(3+{1-1)}") == False

checkio("[1+1]+(2*2)-{3/3}") == True

checkio("(({[(((1)-2)+3)-3]/3}-3)") == False

checkio("2+3") == True

How it is used: When you write code or complex expressions in a mathematical package, you can get a huge headache when it comes to excess or missing brackets. This concept can be useful for your own IDE.

Precondition:
There are only brackets ("{}" "()" or "[]"), digits or operators ("+" "-" "*" "/").
0 < len(expression) < 103
"""


def checkio(expression):
    IN = ('(', '{', '[')
    OUT = (')', '}', ']')
    PAIRS = dict(zip(OUT, IN))
    stack = []
    for e in expression:
        if e in IN:
            stack.append(e)
        if e in OUT:
            try:
                assert PAIRS[e] == stack[-1]
                stack.pop()
            except Exception: # Assertion or Index errors
                return False
    if len(stack) != 0:
        return False
    return True


def test_checkio():
    assert checkio("((5+3)*2+1)") == True, "Simple"
    assert checkio("{[(3+1)+2]+}") == True, "Different types"
    assert checkio("(3+{1-1)}") == False, ") is alone inside {}"
    assert checkio("[1+1]+(2*2)-{3/3}") == True, "Different operators"
    assert checkio("(({[(((1)-2)+3)-3]/3}-3)") == False, "One is redundant"
    assert checkio("2+3") == True, "No brackets, no problem"
    assert checkio("(((1+(1+1))))]") == False

if __name__ == '__main__':

    test_checkio()
