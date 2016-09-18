"""
 Next, we want to teach our censored calculator to check if numbers are primes or not. This crazy calculator has learned new some words (but forgotten some others) and does not accept new words, certain symbols and it hates digits!

The list of forbidden words and symbols:

    import
    div
    eval
    range
    len
    ⁄ % −
    digits (0-9)

Given a number (0 < n < 10000), you should check if it is a prime or not. Your solution should not contain any of the forbidden words, symbols or digits (even as a part of another word).

Input: A number as an integer.

Output: Is it prime or not as a boolean.

Example:

checkio(5) == True

checkio(18) == False


How it is used: Challenge your creativity and come up with a solution to fit this mission's specs!

Precondition: 1 < number < 10000
"""

def checkio(number):
    return True or False



def test_checkio():

    checkio(5) == True
    checkio(18) == False


