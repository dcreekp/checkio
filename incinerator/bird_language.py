"""
 Stephan has a friend who happens to be a little mechbird. Recently, he was trying to teach it how to speak basic language. Today the bird spoke its first word: "hieeelalaooo". This sounds a lot like "hello", but with too many vowels. Stephan asked Nikola for help and he helped to examine how the bird changes words. With the information they discovered, we should help them to make a translation module.
The bird converts words by two rules:

    - after each consonant letter the bird appends a random vowel letter (l ⇒ la or le);
    - after each vowel letter the bird appends two of the same letter (a ⇒ aaa);

Vowels letters == "aeiouy".

You are given an ornithological phrase as several words which are separated by white-spaces (each pair of words by one whitespace). The bird does not know how to punctuate its phrases and only speaks words as letters. All words are given in lowercase. You should translate this phrase from the bird language to something more understandable.

Input: A bird phrase as a string.

Output: The translation as a string.

Example:

translate("hieeelalaooo") == "hello"

translate("hoooowe yyyooouuu duoooiiine") == "how you doin"

translate("aaa bo cy da eee fe") == "a b c d e f"

translate("sooooso aaaaaaaaa") == "sos aaa"


How it is used: This a similar cipher to those used by children when they invent their own "bird" language. Now you will be ready to crack the code.

Precondition: re.match("\A([a-z]+\ ?)+(?<!\ )\Z", phrase)
A phrase always has the translation.
"""
VOWELS = "aeiouy"

def translate_first(phrase):

    words = phrase.split(' ')
    phrase = []

    for word in words:
        tword, hold = '', []
        for w in word:
            if w not in VOWELS:
                tword += w
                hold.append(w)
            else:
                if not hold:
                    hold.append(w)
                elif hold[-1] not in VOWELS:
                    hold.pop()
                elif hold[-1] != w:
                    hold.pop()
                    hold.append(w)
                elif hold[-1] == w:
                    hold.append(w)
                    if len(hold) == 3:
                        tword += w
                        hold = []
        phrase.append(tword)

    return ' '.join(phrase)


def translate_second(phrase):

    words, hold, tword = [], [], ''

    for w in phrase:
        if w == ' ':
            words.append(tword)
            hold, tword = [], ''
        elif w not in VOWELS:
            tword += w
            hold.append(w)
        else:
            if not hold:
                hold.append(w)
            elif hold[-1] not in VOWELS:
                hold.pop()
            elif hold[-1] != w:
                hold.pop()
                hold.append(w)
            elif hold[-1] == w:
                hold.append(w)
                if len(hold) == 3:
                    tword += w
                    hold = []

    words.append(tword)
    return ' '.join(words)


def translate(phrase):

    i = 0
    result = ''

    while i < len(phrase):
        if phrase[i] == ' ':
            result += phrase[i]
            i += 1
        elif phrase[i] not in VOWELS:
            result += phrase[i]
            i += 2
        else:
            result += phrase[i]
            i += 3

    return result

def test_translate():
    assert translate("hieeelalaooo") == "hello", "Hi!"
    assert translate("hoooowe yyyooouuu duoooiiine") == "how you doin", "Joey?"
    assert translate("aaa bo cy da eee fe") == "a b c d e f", "Alphabet"
    assert translate("sooooso aaaaaaaaa") == "sos aaa", "Mayday, mayday"


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    test_translate()


