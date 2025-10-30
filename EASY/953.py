# 953. Verifying an Alien Dictionary

# In an alien language, surprisingly, they also use English lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

# Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographically in this alien language.

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        ind = {c : i for i, c in enumerate(order)}

        for i in range(len(words) - 1):
            i1, i2 = words[i], words[i + 1]

            for j in range(len(i1)):
                if j == len(i2):
                    return False
                if i1[j] != i2[j]:
                    if ind[i2[j]] < ind[i1[j]]:
                        return False
                    break
        return True