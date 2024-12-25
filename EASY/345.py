# 345. Reverse Vowels of a String

# Given a string s, reverse only all the vowels in the string and return it.

# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        vowels = set('aeiouAEIOU')
        l, r = 0, len(s) - 1
        while l < r:
            if s[l].lower() in vowels:
                if s[r].lower() in vowels:
                    s[l], s[r] = s[r], s[l]
                    l += 1
                    r -= 1
                else:
                    r -= 1
            else:
                l += 1
        return "".join(s)