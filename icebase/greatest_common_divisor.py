# -*- coding: utf-8 -*-
"""
 The greatest common divisor (GCD), also known as the greatest common factor of two or more integers (at least one of which is not zero), is the largest positive integer that divides a number without a remainder. For example, the GCD of 8 and 12 is 4.

You are given an arbitrary number of positive integers. You should find the greatest common divisor for these numbers.

Input: An arbitrary number of positive integers.

Output: The greatest common divisor as an integer.

Example:

great_common_divisor(6, 4) == 2

great_common_divisor(2, 4, 8) == 2


How it is used: GCD is a basic concept found in mathematically oriented software. This is a good example of a simple algorithm which has many possible applications.

Precondition:
1 < len(args) ≤ 10
all(0 < x ≤ 2 ** 32 for x in args)
"""

def great_common_divisor1(*args):

    def gcd(a, b, d=1):
        if a == b:
            return a * d
        if a % b == 0:
            return b * d
        if b % a == 0:
            return a * d
        if a % 2 == 0 and b % 2 == 0:
            return gcd(a/2, b/2, d*2)
        if a % 2 == 0 and b % 2 != 0:
            return gcd(a/2, b, d)
        if a % 2 != 0 and b % 2 == 0:
            return gcd(a, b/2, d)
        if a % 2 != 0 and b % 2 != 0 and b > a:
            return gcd(a, (b-a)/2, d)


    args = sorted(args)
    while len(args) > 2:
        args = [gcd(args[0], args[1])] + args[2:]
    else:
        return gcd(args[0],args[1])

def test1():
    assert great_common_divisor1(6, 4) == 2
    assert great_common_divisor1(18, 3600) == 18
    assert great_common_divisor1(4, 8, 16) == 4
    assert great_common_divisor1(11, 13) == 1
    assert great_common_divisor1(11, 13, 17, 19, 23, 29, 31, 37, 41, 43) == 1


def great_common_divisorE(*args):

    def gcd(a, b):
        while a % b != 0:
            a, b = b, a % b
        return b

    def gcdR(a,b):
        if a % b != 0:
            return gcd(b, a % b)
        else:
            return b

    args = list(args)
    while len(args) > 2:
        args = [gcdR(args[0], args[1])] + args[2:]
    else:
        return gcdR(args[0],args[1])


def test2():
    assert great_common_divisorE(6, 4) == 2
    assert great_common_divisorE(18, 3600) == 18
    assert great_common_divisorE(16, 8, 4) == 4
    assert great_common_divisorE(11, 13) == 1
    assert great_common_divisorE(11, 13, 17, 19, 23, 29, 31, 37, 41, 43) == 1


if __name__ == '__main__':

    try:
        test1()
        test2()
    except AssertionError as e:
        raise(e)
    else:
        print('all good')



