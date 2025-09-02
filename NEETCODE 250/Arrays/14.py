# 14. Longest Common Prefix

# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for i in range(len(prefix)):
            for j in strs:
                if i == len(j) or prefix[i] != j[i]:
                    return prefix[:i]
        return prefix

        # res = ""
        # for i in range(len(strs[0])):
        #     for j in strs:
        #         if i == len(j) or j[i] != strs[0][i]:
        #             return res
        #     res += strs[0][i]
        # return res