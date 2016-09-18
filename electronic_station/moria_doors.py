"""
 You are given a message. You need to pick out all words (a consecutive sequence of letters or a single letter), calculate the "likeness" coefficients with other words, take an average of them and choose the greatest. Count "likeness" coefficient even for the same words (of course it's 100). If several words have the same resulting value, then choose the word closest to the end of the message. Words in the message can be separated by whitespaces and punctuation. There are no numbers.

"Likeness" coefficient for two words is measured in percentages using the following rules:
- Letter case does not matter ("A" == "a");
- If the first letters of the words are equal, then add 10%;
- If the last letters of the words are equal, then add 10%;
- Add length comparison as
(length_of_word1 / length_of_word2) * 30%, if length_of_word1 ≤ length_of_word2;
, else (length_of_word2 / length_of_word1) * 30%
- Take all unique letters from the both words in one set and count how many letters appear in the both words. Add to the coefficient (common_letter_number / unique_letters_numbers) * 50;

So the maximum coefficient of likeness is 100%. For example: for the words "Bread" and "Beard".

The result should be given in the lower case.

Let's look at an example. The message "Friend Fred and friend Ted." First, pick out words - ("friend", "fred", "and", "friend", "ted"). Next we calculate "likeness" for the first word with other. "friend" and "fred" have the same first and last letters, so add 20. Then length comparison: the length of "fred" is lesser than "friend", so add (4/6)*30=20. The last rule: for these words unique letters are "definr" and the intersected letters are "defr". So add (4/6)*50≈33.333. And the summary is 73.333.
This way we will count all other coefficients and get the following table (results are rounded just for simplicity). The greatest average is 62.976 and the result is "friend".

        | friend  | fred    | and     | friend  | ted     |
--------|---------|---------|---------|---------|---------|
friend  | ------  | 73.333  | 39.286  | 100.0   | 39.286  |
fred    | 73.333  | ------  | 40.833  | 73.333  | 52.5    |
and     | 39.286  | 40.833  | ------  | 39.286  | 50.0    |
friend  | 100.0   | 73.333  | 39.286  | ------  | 39.286  |
ted     | 39.286  | 52.5    | 50.0    | 39.286  | ------  |
--------|---------|---------|---------|---------|---------|
sum     | 251.905 | 239.999 | 169.405 | 251.905 | 181.072 |
average | 62.976  | 60      | 42.351  | 62.976  | 45.268  |

Input: A message as a string (unicode)

Output: The keyword as a string.

Example:

find_word("Speak friend and enter.") == "friend"


How it is used: This is a fabricated algorithm which can be modified and be used for linguistic research and text pattern recognition.

Precondition:
0 < len(message)
all(x in (string.ascii_letters + string.punctuation + " ") for x in message)
"""

import string

def find_word(message):

    message = message.lower().split(' ')
    message = [word.strip(string.punctuation) for word in message]

    best = 0
    the_word = ""

    for i in range(len(message)):
        check = message.pop()
        total = 0
        for word in message:
            if check[0] == word[0]:
                total += 10
            if check[-1] == word[-1]:
                total += 10
            length = min(len(check), len(word)) / max(len(check), len(word))
            total += length * 30
            both = len(set(check) | set(word)) #union
            common = len(set(check) & set(word)) # intersection
            # both = len(set(check)) + len(set(word))
            # unique = len(set(list(set(check)) + list(set(word))))
            # common = both - unique
            total += common / both * 50
        if total > best:
            best = total
            the_word = check
        message = [check] + message

    return the_word

def test_moria_doors():

    assert find_word("Speak friend and enter.") == "friend", "Friend"
    assert find_word("Beard and Bread") == "bread", "Bread is Beard"
    assert find_word("The Doors of Durin, Lord of Moria. Speak friend and enter. "
                     "I Narvi made them. Celebrimbor of Hollin drew these signs") == "durin", "Durin"
    assert find_word("Aoccdrnig to a rscheearch at Cmabrigde Uinervtisy."
                     " According to a researcher at Cambridge University.") == "according", "Research"
    assert find_word("One, two, two, three, three, three.") == "three", "Repeating"


if __name__ == '__main__':

    test_moria_doors()
