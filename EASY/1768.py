# 1768. Merge Strings Alternately

# You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

# Return the merged string.

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i, j = 0, 0
        l = []
        while i < len(word1) and j < len(word2):
            l.append(word1[i])
            i += 1
            l.append(word2[j])
            j += 1
        
        while i < len(word1):
            l.append(word1[i])
            i += 1
        while j < len(word2):
            l.append(word2[j])
            j += 1
        return "".join(l)
            