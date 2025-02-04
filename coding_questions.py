# Anagram
# Defination
# A word w is an anagram of a word v if a permutation of the letters transforming w
# into v exists. Given a set of n words of length at most k, we would like to detect all
# possible anagrams.

# input: below the car is a rat drinking cider and bending its elbow while this thing
# is an arc that can act like a cat which cried during the night caused by pain in its
# bowel1
# `output`: {bowel below elbow}, {arc car}, {night thing}, {cried cider}, {act cat}

# Algorithm
# The idea is to compute a signature for each word,
# so that two words are anagrams of
# each other if and only if they have the same signature.
# This signature is simply a new
# string made up of the same letters sorted in lexicographical order.
# The data structure used is a dictionary associating with each signature the list of
# words with this signature.

def anagram(S):
    # Split the input string into words
    words = S.split()

    # Dictionary to group anagrams
    d = {}
    for word in words:
        # Sort the characters of the word to create a key
        s = ''.join(sorted(word))
        if s in d:
            d[s].append(word)
        else:
            d[s] = [word]

    # Return groups of anagrams with more than 1 word (or adjust the threshold as needed)
    return [d[s] for s in d if len(d[s]) > 1]


# Input string
text = '''below the car is a rat drinking cider and bending its elbow while this thing
is an arc that can act like a cat which cried during the night caused by pain in its
bowel'''

# Call the function and print the result
print(anagram(text))