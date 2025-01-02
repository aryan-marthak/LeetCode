# 409. Longest Palindrome

# Given a string s which consists of lowercase or uppercase letters, return the length of the longest
# palindrome
#  that can be built with those letters.

# Letters are case sensitive, for example, "Aa" is not considered a palindrome.

class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = defaultdict(int)
        res = 0
        for c in s:
            count[c] += 1
            if count[c] % 2 == 0:
                res += 2
        for cnt in count.values():
            if cnt % 2:
                res += 1
                break
        return res