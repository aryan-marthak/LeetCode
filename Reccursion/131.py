# 131. Palindrome Partitioning

# Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def ispali(s):
            return True if s == s[::-1] else False
        def backtrack(start, path):
            if start >= len(s):
                res.append(path[:])
                return
            for j in range(start, len(s)):
                if ispali(s[start:j+1]):
                    path.append(s[start:j+1])
                    backtrack(j+1, path)
                    path.pop()

        backtrack(0, [])
        return res