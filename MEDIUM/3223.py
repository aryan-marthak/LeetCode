# 3223. Minimum Length of String After Operations

# You are given a string s.

# You can perform the following process on s any number of times:

#     Choose an index i in the string such that there is at least one character to the left of index i that is equal to s[i], and at least one character to the right that is also equal to s[i].
#     Delete the closest occurrence of s[i] located to the left of i.
#     Delete the closest occurrence of s[i] located to the right of i.

# Return the minimum length of the final string s that you can achieve.

class Solution:
    def minimumLength(self, s: str) -> int:
        res = 0

        for i in Counter(s).values():
            if i % 2 == 1:
                res += 1
            else:
                res += 2
        return res