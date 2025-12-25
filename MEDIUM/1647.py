# 1647. Minimum Deletions to Make Character Frequencies Unique

# A string s is called good if there are no two different characters in s that have the same frequency.

# Given a string s, return the minimum number of characters you need to delete to make s good.

# The frequency of a character in a string is the number of times it appears in the string. For example, in the string "aab", the frequency of 'a' is 2, while the frequency of 'b' is 1.

class Solution:
    def minDeletions(self, s: str) -> int:
        count = Counter(s)
        res = 0
        Set = set()
        for i, j in count.items():
            while j > 0 and j in Set:
                j -= 1
                res += 1
            Set.add(j)
        return res