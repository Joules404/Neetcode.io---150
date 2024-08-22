#grouping anagrams 
from collections import defaultdict
words = ["act","pots","tops","cat","stop","hat"]

def group_anagrams(list_of_words):
    hashmap = defaultdict(list)
    #mapping charCount for each string to list of Anagrams
    for word in list_of_words:
        alpha = [0] * 26
        for ch in word:
            alpha[ord(ch) - ord("a")]+=1
        hashmap[tuple(alpha)].append(word)
    print(hashmap.values())
    return hashmap.values()

group_anagrams(words)