# 1400. Construct K Palindrome Strings

# Given a string s and an integer k, return true if you can use all the characters in s to construct non-empty k
# or false otherwise.

class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if k > len(s):
            return False
        
        count = Counter(s)
        odd = 0
        for i in count.values():
            if i % 2:
                odd += 1
        return odd <= k