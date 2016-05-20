"""
You are given a text, which contains different english letters
and punctuation symbols. You should find the most frequent letter
in the text. The letter returned must be in lower case.
While checking for the most wanted letter, casing does not matter,
so for the purpose of your search, "A" == "a". Make sure you do not
count punctuation symbols, digits and whitespaces, only letters.

If you have two or more letters with the same frequency, then return
the letter which comes first in the latin alphabet. For example -- "one"
contains "o", "n", "e" only once for each, thus we choose "e".

Input: A text for analysis as a string (unicode for py2.7).

Output: The most frequent letter in lower case as a string.

Precondition:
A text contains only ASCII symbols.
0 < len(text) ≤ 105
"""

def checkio(text):

    text = text.lower()

    new = [ t for t in text if t.isalpha()] #in 'qwertyuiopasdfghjklzxcvbnm']

    calc = dict(zip([n for n in new],[new.count(n) for n in new]))

    mm = max(calc.values())

    most_lst = [key for key in calc if calc[key] == mm]

    rank = sorted(most_lst)

    return rank[0]

def test():

    assert checkio("Hello 000000000World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    assert checkio("a" * 9 + "b" * 10) == "b", "Long."


def checkio_r(text):
    """
    We iterate through latin alphabet and count each letter in the text.
    Then 'max' selects the most frequent letter.
    For the case when we have several equal letter,
    'max' selects the first from they.
    """
    import string
    text = text.lower()
    return max(string.ascii_lowercase, key=text.count)

def test_r():

    assert checkio_r("Hello 000000000World!") == "l", "Hello test"
    assert checkio_r("How do you do?") == "o", "O is most wanted"
    assert checkio_r("One") == "e", "All letter only once."
    assert checkio_r("Oops!") == "o", "Don't forget about lower case."
    assert checkio_r("AAaooo!!!!") == "a", "Only letters."
    assert checkio_r("abe") == "a", "The First."
    assert checkio_r("a" * 9 + "b" * 10) == "b", "Long."


def checkio_r2(text):
    letters = "abcdefghijklmnopqrstuvwxyz"
    wanted_letter = ""
    most_times = 0
    for letter in letters:
        times = 0
        for char in text:
            if (char.lower()) == letter:
                times += 1
        if (most_times == times):
            if (wanted_letter > letter):
                wanted_letter = letter
        elif (most_times < times):
            most_times = times
            wanted_letter = letter
    return wanted_letter

def test_r2():

    assert checkio_r2("Hello 000000000World!") == "l", "Hello test"
    assert checkio_r2("How do you do?") == "o", "O is most wanted"
    assert checkio_r2("One") == "e", "All letter only once."
    assert checkio_r2("Oops!") == "o", "Don't forget about lower case."
    assert checkio_r2("AAaooo!!!!") == "a", "Only letters."
    assert checkio_r2("abe") == "a", "The First."
    assert checkio_r2("a" * 9 + "b" * 10) == "b", "Long."


if __name__ == "__main__":

    try:
        test()
        test_r()
        test_r2()
    except AssertionError as e:
        raise(e)
    else:
        print('all good')



