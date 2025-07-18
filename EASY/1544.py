# 1544. Make The String Great

# Given a string s of lower and upper case English letters.

# A good string is a string which doesn't have two adjacent characters s[i] and s[i + 1] where:

#     0 <= i <= s.length - 2
#     s[i] is a lower-case letter and s[i + 1] is the same letter but in upper-case or vice-versa.

# To make the string good, you can choose two adjacent characters that make the string bad and remove them. You can keep doing this until the string becomes good.

# Return the string after making it good. The answer is guaranteed to be unique under the given constraints.

# Notice that an empty string is also good.

# BRUTE FORCE APPROACH

class Solution:
    def makeGood(self, s: str) -> str:
        i = 0
        n = len(s)
        while i < n:
            if i and s[i] != s[i - 1] and s[i].lower() == s[i - 1].lower():
                s = s[:i - 1] + s[i + 1:]
                n -= 2
                i -= 2
            i += 1
        return s 

# STACK Approach

class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        i = 0
        while i < len(s):
            if stack and s[i] != stack[-1] and s[i].lower() == stack[-1].lower():
                stack.pop()
            else:
                stack.append(s[i])
            i += 1
        
        return "".join(stack)
    
