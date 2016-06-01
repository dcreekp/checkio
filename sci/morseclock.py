"""
"di-dah di-di-di-dit di-dah-dah di-dah-dah-dah dah-di-dit dah-di-di-dah", sound of Morszelizer clanked out loud.

"What're you doing?" Nikola asked curiously.

"I'm sending our time logs for the last expedition to headquarters, but it's not an easy task..." Stephen grumbled, "Can you imagine that with all the computer power at our disposal, I STILL have to convert this message to Morse-code with only an on/off button... Hrmph... what a pain." He grumbled at the inconvenience.

"Let me look at it." Nikola offered his help, "It looks like a pretty easy solution, we could automate the process."

"Oh.. you hero of my day." Stephen started excitedly. "So, how do we start it?"

"With Python!" Nikola exclaimed.

Help Stephen to create a module for converting a normal time string to a morse time string. As you can see in the illustration, a gray circle means on, while a white circle means off. Every digit in the time string contains a different number of slots. The first digit for the hours has a length of 2 while the second digit for the hour has a length of 4. The first digits for the minutes and seconds have a length of 3 while the second digits for the minutes and seconds have a length of 4. Every digit in the time is converted to binary representation. You will convert every on (or 1) signal to dash ("-") and every off (or 0) signal to dot (".").


 An time string could be in the follow formats: "hh:mm:ss", "h:m:s" or "hh:m:ss". The "missing" digits are zeroes. For example, "1:2:3" is the same as "01:02:03".
The result will be a morse time string with specific format:

"h h : m m : s s"

where each digits represented as sequence of "." and "-"

Input: A normal time string as a string (unicode).
Output: The morse time string as a string.

Example:

checkio("10:37:49") == ".- .... : .-- .--- : -.. -..-"

checkio("21:34:56") == "-. ...- : .-- .-.. : -.- .--."

checkio("00:1:02") == ".. .... : ... ...- : ... ..-."

checkio("23:59:59") == "-. ..-- : -.- -..- : -.- -..-"

How it is used: Did you see the binary clocks task earlier? This is can be a fun gift for any geek. We tried to combine the old good Morse code with a binary clock in this task, and now you can create the new more complex binary clock, which doesn't show time -- but makes morse style bips and beeps. ;-)

Precondition:
time_string contains correct time.
"""
"""
0 = 0
1 = 1
2 = 10
3 = 11
4 = 100
5 = 101
6 = 110
7 = 111
8 = 1000
9 = 1001
10 = 1010
11 = 1011
12 = 1100
13 = 1101
14 = 1111
15 = 10000
16 = 10001
17 = 10010
18 = 10011
19 = 10100
20 = 10101
21 = 10111
22 = 11000
23 = 11001
"""

def ten_to_two(b10, b2=''):
    """ To convert from a base-10 integer numeral to its base-2 (binary)
        equivalent, the number is divided by two, and the remainder is the
        least-significant bit. The (integer) result is again divided by two,
        its remainder is the next least significant bit. This process repeats
        until the quotient becomes zero.
        https://en.wikipedia.org/wiki/Binary_number
    """
    if b10 != 0:
        b2 += str(b10 % 2)
        b10 //= 2
        return ten_to_two(b10, b2)
    if b2 == '':
        b2 = '0'
    return b2[::-1]


def test_ten_to_two():
    assert ten_to_two(0) == '0'
    assert ten_to_two(15) == '1111'
    assert ten_to_two(1) == '1'
    assert ten_to_two(2) == '10'
    assert ten_to_two(3) == '11'


def checkio(time_string):

    time = []
    for tt in time_string.split(':'):
        if len(tt) == 1:
            tt = '0' + tt
        time.append(tt)

    time_string = ':'.join(time)

    digits = []
    for t in time_string:
        try:
            t = ten_to_two(int(t))
        except ValueError:
            pass # no need to convert ':'
        digits.append(t)

    length = {0:2, 1:4, 2:1, 3:3, 4:4, 5:1, 6:3, 7:4}
    morse = []
    for i, d in enumerate(digits):
        while len(d) < length[i]:
            d = '.' + d
        morse.append(d)

    morse = ' '.join(morse)
    morse = morse.replace('0', '.').replace('1', '-')
    return morse

def test_checkio():
    assert checkio("10:37:49") == ".- .... : .-- .--- : -.. -..-", "First Test"
    assert checkio("21:34:56") == "-. ...- : .-- .-.. : -.- .--.", "Second Test"
    assert checkio("00:1:02") == ".. .... : ... ...- : ... ..-.", "Third Test"
    assert checkio("23:59:59") == "-. ..-- : -.- -..- : -.- -..-", "Fourth Test"


if __name__ == '__main__':

    try:
        test_checkio()
    except AssertionError as e:
        raise(e)
    else:
        print('all good')


