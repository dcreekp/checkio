"""
Sofia has given you a schedule and two dates and told you she needs help planning her weekends. She has asked you to count each day of rest (Saturday and Sunday) starting from the initial date to final date. You should count the initial and final dates if they fall on a Saturday or Sunday.

The dates are given as datetime.date (Read about this module here). The result is an integer.

Input: Start and end date as datetime.date.

Output: The quantity of the rest days as an integer.

Example:

checkio(date(2013, 9, 18), date(2013, 9, 23)) == 2

checkio(date(2013, 1, 1), date(2013, 2, 1)) == 8

checkio(date(2013, 2, 2), date(2013, 2, 3)) == 2

How it is used: Now is a good time to learn how to work with dates. These ideas here often come up in calendar apps, customer relation management software, automated messaging schedulers among many other things.

Precondition: start_date < end_date.

"""

from datetime import date


def checkio(from_date, to_date):
    """
        Count the days of rest
    """
    count = 0

    from_date = from_date.toordinal()
    to_date = to_date.toordinal()

    for day in range(from_date, to_date + 1):
        if date.fromordinal(day).weekday() > 4:
            count += 1

    return count

def test():

    assert checkio(date(2013, 9, 18), date(2013, 9, 23)) == 2, "1st example"
    assert checkio(date(2013, 1, 1), date(2013, 2, 1)) == 8, "2nd example"
    assert checkio(date(2013, 2, 2), date(2013, 2, 3)) == 2, "3rd example"


from datetime import date, timedelta

def checkio_r(from_date, to_date):
    """
        Count the days of rest
    """
    ret = 0
    delta = timedelta(days = 1)
    while from_date <= to_date:
        if from_date.weekday() >= 5:
            ret += 1
        from_date += delta
    return ret

def test_r():

    assert checkio_r(date(2013, 9, 18), date(2013, 9, 23)) == 2, "1st example"
    assert checkio_r(date(2013, 1, 1), date(2013, 2, 1)) == 8, "2nd example"
    assert checkio_r(date(2013, 2, 2), date(2013, 2, 3)) == 2, "3rd example"


if __name__ == '__main__':

    try:
        test()
        test_r()
    except AssertionError as e:
        raise(e)
    else:
        print('all good')
