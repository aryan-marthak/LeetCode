# 28. Find the index of first occurrence in a string

# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

class Solution(object):
    def strStr(self, haystack, needle):
        if needle == "":
            return 0
        if needle in haystack:
            return haystack.index(needle)
        return -1