from collections import Counter

word = 'Hello'

def count_letters(word):
    c = Counter()
    for w in word:
        c[word] += 1
    return c

print(count_letters(word))
