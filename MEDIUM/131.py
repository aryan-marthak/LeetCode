# 131. Palindrome Partitioning

# Given a string s, partition s such that every substring of the partition is a pallindrome. Return all possible palindrome partitioning of s.

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def ispali(word): 
            i, j = 0, len(word) - 1
            while i < j:
                if word[i] != word[j]:
                    return False
                i += 1
                j -= 1
            return True
        
        res = []

        def bt(i, curr):
            if i >= len(s):
                res.append(curr.copy())

            for j in range(i, len(s)):
                part = s[i:j + 1]

                if ispali(part):
                    curr.append(part)
                    bt(j + 1, curr)
                    curr.pop()
        bt(0, [])
        return res

# Time complexity: O(n * 2^n)
# Space complexity: O(n)