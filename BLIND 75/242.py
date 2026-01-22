# 242. Valid Anagram

# Given two strings s and t, return true if t is an
# of s, and false otherwise.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)

        
        # if len(s) != len(t):
        #     return False
        # for i in set(s):
        #     if s.count(index) != t.count(index):
        #         return False
        # return True  
        

        # if len(s) != len(t):
        #     return False
        # dictionary = {}
        # for i in s:
        #     dictionary[i] = dictionary.get(i, 0) + 1
        # for i in t:
        #     if i not in dictionary or dictionary[i] == 0:
        #         return False
        #     dictionary[i] -= 1
        # return True