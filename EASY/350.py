# 350. Intersection of Two Arrays II

# Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        for i in nums2:
            if i in nums1:
                ans.append(i)
                nums1.remove(i)
        return ans
    
# using counter object

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        c = Counter(nums1)
        output = []
        for n in nums2:
            if c[n] > 0:
                output.append(n)
                c[n] -= 1
        return output 