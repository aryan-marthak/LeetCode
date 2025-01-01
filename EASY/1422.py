# 1422. Maximum Score After Splitting a String

# Given a string s of zeros and ones, return the maximum score after splitting the string into two non-empty substrings (i.e. left substring and right substring).

# The score after splitting a string is the number of zeros in the left substring plus the number of ones in the right substring.



# brute force approach (splitting string into left and right, finding no. of zeroes and ones in left and right, sum and compare with a max variable)

class Solution:
    def maxScore(self, s: str) -> int:
        Max = 0 
        for i in range(1, len(s)):
            left = s[:i]
            right = s[i:]

            zeros = 0
            ones = 0

            for a in left:
                if a == '0':
                    zeros += 1
            for a in right:
                if a == '1':
                    ones += 1
            x = zeros + ones
            if x > Max:
                Max = x
        return Max
    
    
# neetcode approach (split the string from the start, count the no. of ones already, iterate through all the split points while checking if the new index has zero or one, if it is zero increment no. of zeros keeping the no. of ones the same, and if it is a one, reduce the count of ones)

        zero = 0
        one = s.count("1")
        res = 0

        for i in range(len(s) - 1):
            if s[i] == "0":
                zero += 1
            else:
                one -= 1
            res = max(res, zero + one)
        return res