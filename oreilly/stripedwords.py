"""
Our robots are always working to improve their linguistic skills. For this mission, they research the latin alphabet and its applications.

The alphabet contains both vowel and consonant letters (yes, we divide the letters).
Vowels -- A E I O U Y
Consonants -- B C D F G H J K L M N P Q R S T V W X Z

You are given a block of text with different words. These words are separated by white-spaces and punctuation marks. Numbers are not considered words in this mission (a mix of letters and digits is not a word either). You should count the number of words (striped words) where the vowels with consonants are alternating, that is; words that you count cannot have two consecutive vowels or consonants. The words consisting of a single letter are not striped -- do not count those. Casing is not significant for this mission.

Input: A text as a string (unicode)

Output: A quantity of striped words as an integer.

Example:
checkio("My name is ...") == 3
checkio("Hello world") == 0
checkio("A quantity of striped words.") == 1, "Only of"
checkio("Dog,cat,mouse,bird.Human.") == 3

How it is used: This idea in this task is a useful exercise for linguistic research and analysis. Text processing is one of the main tools used in the analysis of various books and languages and can help translate print text to a digital format.

Precondition:The text contains only ASCII symbols.
0 < len(text) < 105
"""

from string import punctuation
VOWELS = "AEIOUY"
CONSONANTS = "BCDFGHJKLMNPQRSTVWXZ"


def checkio(text):

    for p in punctuation:
        text = text.replace(p, ' ')
    text = text.upper()
    lst = [word for word in text.split() if word.isalpha()]

    count = 0
    for word in lst:
        if parse(word):
            count += 1

    return count

def parse(word):

    if len(word) <= 1:
        return None

    vowels = set(VOWELS)
    consonants = set(CONSONANTS)
    odd = set(a for a in word[::2])
    even = set(b for b in word[1::2])

    if odd <= vowels and even <= consonants:
        return True
    elif odd <= consonants and even <= vowels:
        return True
    else:
        return None

def test():

    assert checkio("My name is ...") == 3, "All words are striped"
    assert checkio("Hello world") == 0, "No one"
    assert checkio("A quantity of 87654striped words.") == 1, "Only of"
    assert checkio("Dog,cat,mou5se,bird.Human.") == 3, "Dog, cat and human"


VOWELS = "AEIOUY"
CONSONANTS = "BCDFGHJKLMNPQRSTVWXZ"
PUNCTUATION = ",.!?"

def checkio_r(text):
    text = text.upper()
    for c in PUNCTUATION:
        text = text.replace( c, " " )
    for c in VOWELS:
        text = text.replace( c, "v" )
    for c in CONSONANTS:
        text = text.replace( c, "c" )

    words = text.split( " " )

    count = 0
    for word in words:
        if len( word ) > 1 and word.isalpha():
            if word.find( "cc" ) == -1 and word.find( "vv" ) == -1:
                count += 1

    return count

def test_r():

    assert checkio_r("My name is ...") == 3, "All words are striped"
    assert checkio_r("Hello world") == 0, "No one"
    assert checkio_r("A quantity of 87654striped words.") == 1, "Only of"
    assert checkio_r("Dog,cat,mou5se,bird.Human.") == 3, "Dog, cat and human"


if __name__ == '__main__':
    try:
        test()
        test_r()
    except AssertionError as e:
        raise(e)
    else:
        print('all good')
