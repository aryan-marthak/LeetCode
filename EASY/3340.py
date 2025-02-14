# 3340. Check Balanced String

# You are given a string num consisting of only digits. A string of digits is called balanced if the sum of the digits at even indices is equal to the sum of digits at odd indices.

# Return true if num is balanced, otherwise return false.

class Solution:
    def isBalanced(self, num: str) -> bool:
        oddsum = 0
        evensum = 0
        for i in range(0, len(num), 2):
            evensum += int(num[i])
        for i in range(1, len(num), 2):
            oddsum += int(num[i])
        return oddsum == evensum
        