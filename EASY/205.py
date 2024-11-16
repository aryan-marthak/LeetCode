# 205. Isomorphic Strings

# Given two strings s and t, determine if they are isomorphic.

# Two strings s and t are isomorphic if the characters in s can be replaced to get t.

# All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map1, map2 = {}, {}

        for i, j in zip(s, t):
            if ((i in map1 and map1[i] != j) or (j in map2 and map2[j] != i)):
                return False
            map1[i] = j
            map2[j] = i
        return True