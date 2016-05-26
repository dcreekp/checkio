"""
 Many countries use different conventions for the thousands separator and decimal mark. For example in the Netherlands one million one thousand two hundred and eighty one-hundredths is written as 1.001.200,80, but in the US this is written as 1,001,200.80. Use your coding skills to convert dollars in the first style (Netherlands, Germany, Russia, Turkey, Brazil, and others) to the second style (US, UK, Canada, China, Japan, Mexico, and others).

Only currency amounts in dollars should be converted: $1.234,50 to $1,234.50, $1.000 to $1,000, and $4,57 to $4.57. But don't convert your router's IP address 192.168.1.1. Also leave currency in the US style unchanged.

Input: A string containing dollar amounts to be converted.

Output: A string with converted currencies.

Example:

    checkio("Lot 192.001 costs $1.000,94.") == "Lot 192.001 costs $1,000.94."

    checkio("$1,23 + $2,34 = $3,57.") == "$1.23 + $2.34 = $3.57."

How it is used: This is an exercise in working with strings and using the Python standard library.

Precondition: 0 < len(text) ≤ 1000;
len(fractional_part_of_currency) in {0,2};
all(s[-1].isdigit() for s in currency_substrings);
all(s[0] == '$' for s in currency_substrings)
"""

def checkio1(text): # DOES NOT WORK
    new_text_lst = []
    for word in text.split(' '):
        if word.startswith('$'):
            if word.endswith(',') and word[-4] == ',':
                word = word.replace('.', ',')
                word = word[::1].replace(',', '.', 2).replace('.', ',', 1)
                word = word[::1]
            elif len(word) > 3 and word[-3] == ',':
                word = word.replace('.', ',')
                word = word[::-1].replace(',', '.', 1)
                word = word[::-1]
            else:
                word = word.replace('.', ',')
        new_text_lst.append(word)

    new_text = ' '.join(new_text_lst)
    return new_text


def checkio2(text): # FIRST ONE THAT WORKS
    new_text_lst = []
    for word in text.split(' '):
        if word.startswith('$'):
            us = ''
            for i, w in enumerate(word):
                try:
                    if w == ',':
                        if word[-1].isdigit() and i + 3 == len(word):
                            w = '.'
                        elif word[-2].isdigit() and i + 4 == len(word):
                            w = '.'
                    if w == '.':
                        if word[i+3].isdigit():
                            w = ','
                except IndexError:
                    pass
                us += w
            word = us
        new_text_lst.append(word)
    new_text = ' '.join(new_text_lst)
    return new_text


def checkio(text): # MY FAVOURITE
    new_text_lst = []
    for word in text.split(' '):
        if word[0] == '$' and (',' in word or '.' in word):
            word = word[::-1].replace('.', '^').replace(',', '^')
            if word[0] == '^':
                word = word.replace('^', ',', 1)
                if word[3] == '^':
                    word = word.replace('^', '.', 1)
            else:
                if word[2] == '^':
                    word = word.replace('^', '.', 1)
            word = word.replace('^', ',')[::-1]
        new_text_lst.append(word)
    new_text = ' '.join(new_text_lst)
    return new_text




def test_checkio():

    assert checkio("$1.234.567,89") == "$1,234,567.89"
    assert checkio("$0,89") == "$0.89"
    assert checkio("Euro Style = $12.345,67, US Style = $12,345.67") == \
                   "Euro Style = $12,345.67, US Style = $12,345.67"
    assert checkio("Us Style = $12,345.67, Euro Style = $12.345,67") == \
                   "Us Style = $12,345.67, Euro Style = $12,345.67"
    assert checkio("$1.234, $5.678 and $9") == \
                   "$1,234, $5,678 and $9"


if __name__ == '__main__':

    checkio("$1.234.567,89")
    checkio("$0,89")
    checkio("$1.234, $5.00,8 and $9")
    checkio("Euro Style = $12.345,67, US Style = $12,345.67")
    try:
        test_checkio()
    except AssertionError as e:
        raise(e)
    else:
        print('all good')
