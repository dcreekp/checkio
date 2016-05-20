"""
An anagram is a type of word play, the result of rearranging the letters of a word or phrase to produce a new word or phrase, using all the original letters exactly once. Two words are anagrams to each other if we can get one from another by rearranging the letters. Anagrams are case-insensitive and don't take account whitespaces. For example: "Gram Ring Mop" and "Programming" are anagrams. But "Hello" and "Ole Oh" are not.

You are given two words or phrase. Try to verify are they anagrams or not.

Input: Two arguments as strings.

Output: Are they anagrams or not as boolean (True or False)

Example:

verify_anagrams("Programming", "Gram Ring Mop") == True

verify_anagrams("Hello", "Ole Oh") == False

verify_anagrams("Kyoto", "Tokyo") == True

How it is used: Anagramming can be a fun way to train your brain, but they have and another application. Psychologists use anagram-oriented tests, often called "anagram solution tasks", to assess the implicit memory. Anagrams are connected to pseudonyms, by the fact that they may conceal or reveal, or operate somewhere in between like a mask that can establish identity. In addition to this, multiple anagramming is a technique sometimes used to solve some kinds of cryptograms.

Precondition: 0 < |first_word| < 100;
0 < |second_word| < 100;
Words contain only ASCII latin letters and whitespaces.
"""


def verify_anagrams(first_word, second_word):

    first_word, second_word = first_word.lower(), second_word.lower()
    first_word, second_word = first_word.replace(' ', ''), second_word.replace(' ', '')

    if sorted(first_word) == sorted(second_word):
        return True
    else:
        return False


def test():

    assert isinstance(verify_anagrams("a", 'z'), bool), "Boolean!"
    assert verify_anagrams("Programming", "Gram Ring Mop") == True, "Gram of code"
    assert verify_anagrams("Hello", "Ole Oh") == False, "Hello! Ole Oh!"
    assert verify_anagrams("Kyoto", "Tokyo") == True, "The global warming crisis of 3002"


def verify_anagrams_r(first_word, second_word):
    f = lambda s: [s.lower().count(c) for c in 'abcdefghijklmnopqrstuvwxyz']
    return f(first_word) == f(second_word)

def test_r():

    assert isinstance(verify_anagrams_r("a", 'z'), bool), "Boolean!"
    assert verify_anagrams_r("Programming", "Gram Ring Mop") == True, "Gram of code"
    assert verify_anagrams_r("Hello", "Ole Oh") == False, "Hello! Ole Oh!"
    assert verify_anagrams_r("Kyoto", "Tokyo") == True, "The global warming crisis of 3002"


if __name__ == '__main__':

    try:
        test()
        test_r()
    except AssertionError as e:
        raise(e)
    else:
        print('all good')
