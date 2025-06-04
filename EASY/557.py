# 557. Reverse Words in a String III

# Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        for i in range(len(s)):
            word = list(s[i])
            l, r = 0, len(word) - 1
            while l < r:
                word[l], word[r] = word[r], word[l]
                l += 1
                r -= 1
            s[i] = "".join(word)
        return " ".join(s)
        
