# https://www.codewars.com/kata/51e056fe544cf36c410000fb/train/python

import re

def top_3_words(text):
    words = {}
    text = re.sub(r"[^A-Za-z0-9' ]+", ' ', text)
    for word in text.lower().split():
        containLetter = False
        for char in word:
            if char.isalpha():
                containLetter = True
                break
        if containLetter:
            if word in words:
                words[word] += words[word] + 1
            else:
                words[word] = 1
    s_words = sorted(words.items(), key=lambda kv: kv[1], reverse=True)[:min(3, len(words.values()))]
    return [pair[0] for pair in s_words]

from collections import Counter

def top_3_words_best(text):
    c = Counter(re.findall(r"[a-z']+", re.sub(r" '+ ", " ", text.lower())))
    return [w for w,_ in c.most_common(3)]

print(top_3_words_best("In a village of La Mancha, the name of which I have no desire to call to mind, there lived not long since one of those gentlemen that keep a lance in the lance-rack, an old buckler, a lean hack, and a greyhound for coursing. An olla of rather more beef than mutton, a salad on most nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra on Sundays, made away with three-quarters of his income."))
print(top_3_words_best("  //wont won't won't "))
print(top_3_words_best("a a a  b  c c  d d d d  e e e e e"))

