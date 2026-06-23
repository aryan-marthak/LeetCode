# 47. Permutations II

# Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        curr = []
        count = {n:0 for n in nums}
        for n in nums:
            count[n] += 1

        def bt():
            if len(curr) == len(nums):
                res.append(curr.copy())
                return
            
            for i in count:
                if count[i] > 0:
                    curr.append(i)
                    count[i] -= 1

                    bt()
                    
                    count[i] += 1
                    curr.pop()
        bt()
        return res