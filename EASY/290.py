# 290. Word Pattern

# Given a pattern and a string s, find if s follows the same pattern.

# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s. Specifically:

#     Each letter in pattern maps to exactly one unique word in s.
#     Each unique word in s maps to exactly one letter in pattern.
#     No two letters map to the same word, and no two words map to the same letter.

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        word = s.split(" ")
        if len(pattern) != len(word):
            return False
        
        charToWord = {}
        wordToChar = {}

        for l, w in zip(pattern, word):
            if l in charToWord and charToWord[l] != w:
                return False
            if w in wordToChar and wordToChar[w] != l:
                return False
            charToWord[l] = w
            wordToChar[w] = l
        return True
