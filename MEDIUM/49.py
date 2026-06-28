# 49. Group Anagrams

# Given an array of strings strs, group the together. You can return the answer in any order.

# Solution 1: Using sorted string as key
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        Dict = defaultdict(list)
        for i in strs:
            sort = "".join(sorted(i))
            Dict[sort].append(i)
        return list(Dict.values())
# Time Complexity: O(N * KlogK) where N is the number of strings in strs and K is the maximum length of a string in strs. Sorting each string takes O(KlogK) time.
# Space Complexity: O(N * K) for the output list and the dictionary.

# Solution 2: Using character count as key
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        Dict = defaultdict(list)
        for i in strs:
            count = [0] * 26
            for j in i:
                count[ord(j) - ord('a')] += 1
            Dict[tuple(count)].append(i)
        return list(Dict.values())
# Time Complexity: O(N * K) where N is the number of strings in strs and K is the maximum length of a string in strs. Counting characters takes O(K) time.
# Space Complexity: O(N * K) for the output list and the dictionary.