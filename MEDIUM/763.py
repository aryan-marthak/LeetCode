# 763. Partition Labels

# You are given a string s. We want to partition the string into as many parts as possible so that each letter appears in at most one part. For example, the string "ababcc" can be partitioned into ["abab", "cc"], but partitions such as ["aba", "bcc"] or ["ab", "ab", "cc"] are invalid.

# Note that the partition is done so that after concatenating all the parts in order, the resultant string should be s.

# Return a list of integers representing the size of these parts.

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        Map = {}
        res = []
        size = 0
        end = 0
        for i, j in enumerate(s):
            Map[j] = i
        for i, j in enumerate(s):
            size += 1
            if Map[j] > end:
                end = Map[j]
            if i == end:
                res.append(size)
                size = 0
        return res