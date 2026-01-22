# 49. Group Anagrams

# Given an array of strings strs, group the
# together. You can return the answer in any order.

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for i in strs:
            res["".join(sorted(i))].append(i)
        return list(res.values())
    
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for i in strs:
            lst = [0] * 26
            for j in i:
                lst[ord(j) - ord('a')] += 1
            lst = tuple(lst)
            res[lst].append(i)
        return list(res.values())