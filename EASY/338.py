# 338. Counting Bits

# Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.


# My own approach

class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for i in range(0, n + 1):
            x = str(bin(i))
            for j in x:
                y = x.count("1")
            ans.append(y)
        return ans