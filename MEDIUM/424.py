# 424. Longest Repeating Character Replacement

# You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

# Return the length of the longest substring containing the same letter you can get after performing the above operations.

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        l = 0
        counts = [0] * 26

        for r in range(len(s)):
            counts[ord(s[r]) - 65] += 1
            while (r - l + 1) - max(counts) > k:
                counts[ord(s[l]) - 65] -= 1
                l += 1
            longest = max(longest, (r - l + 1))
        return longest