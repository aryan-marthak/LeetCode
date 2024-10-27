# 14. Longest Common Prefix
# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        res = ""

        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return res
            res += strs[0][i]
        return res
    


# class Solution:
#     def longestCommonPrefix(self, strs: List[str]) -> str:
#         if not strs:
#             return ""
        
#         prefix = strs[0]
#         for string in strs[1:]:
#             while not string.startswith(prefix):
#                 prefix = prefix[:-1]
#                 if not prefix:
#                     return ""
#         return prefix
