"""
 A pangram (Greek:παν γράμμα, pan gramma, "every letter") or holoalphabetic
 sentence for a given alphabet is a sentence using every letter of the
 alphabet at least once. Perhaps you are familiar with the well known pangram
 "The quick brown fox jumps over the lazy dog".

For this mission, we will use the latin alphabet (A-Z). You are given a text
with latin letters and punctuation symbols. You need to check if the sentence
is a pangram or not. Case does not matter.

Input: A text as a string.

Output: Whether the sentence is a pangram or not as a boolean.

Example:

check_pangram("The quick brown fox jumps over the lazy dog.") == True

check_pangram("ABCDEF.") == False

How it is used: Pangrams have been used to display typefaces, test equipment,
and develop skills in handwriting, calligraphy, and keyboarding for ages.

Precondition:

all(ch in (string.punctuation + string.ascii_letters + " ") for ch in text)

0 < len(text)
"""

def check_pangram(text):
    import string
    check = set(string.ascii_lowercase)
    text = set(c for c in text.lower() if c not in string.punctuation + ' ')
    return check == text




def test_check_pangram():
    assert check_pangram("The quick brown fox jumps over the lazy dog."), "brown fox"
    assert not check_pangram("ABCDEF"), "ABC"
    assert check_pangram("Bored? Craving a pub quiz fix? Why, just come to the Royal Oak!"), "Bored?"


