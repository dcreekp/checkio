"""
 You should write a function to calculate the area of simple figures: circles, rectangles and triangles. You are give an arbitrary number of arguments and depending on this, the function calculates area for the different figures.

    One argument -- The diameter of a circle and you need calculate the area of the circle.

    Two arguments -- The side lengths of a rectangle and you need calculate the area of the rectangle.

    Three arguments -- The lengths of each side on a triangle and you need calculate the area of the triangle.

"""

def simple_areas(*args):

    if len(args) == 3:
        s = sum(args) / 2.0
        return round((s*(s-args[0])*(s-args[1])*(s-args[2]))**0.5, 2)
    elif len(args) == 2:
        return args[0] * args[1]
    else:
        from math import pi
        return round((args[0]/2.0)**2 * pi, 2)


def test():
    assert simple_areas(3) == 7.07
    assert simple_areas(2, 2) == 4
    assert simple_areas(2, 3) == 6
    assert simple_areas(3, 5, 4) == 6
    assert simple_areas(1,1,1) == 0.43
    assert simple_areas(1.5, 2.5, 2) == 1.5


if __name__ == '__main__':

    try:
        test()
    except AssertionError as e:
        raise(e)
    else:
        print('all good')
