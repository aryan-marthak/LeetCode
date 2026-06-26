# 698. Partition to K Equal Sum Subsets

# Given an integer array nums and an integer k, return true if it is possible to divide this array into k non-empty subsets whose sums are all equal.

# Pruning and Backtracking (Pruning is used to avoid unnecessary computations by skipping over certain branches of the search space that cannot lead to a valid solution.)
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k != 0:
            return False

        nums.sort(reverse=True)
        target = total // k
        used = [False] * len(nums)

        def backtrack(i, k, subsetSum):
            if k == 0:
                return True
            if subsetSum == target:
                return backtrack(0, k - 1, 0)
            for j in range(i, len(nums)):
                if used[j] or subsetSum + nums[j] > target:
                    continue
                used[j] = True
                if backtrack(j + 1, k, subsetSum + nums[j]):
                    return True
                used[j] = False

                if subsetSum == 0: # Pruning
                    return False

            return False

        return backtrack(0, k, 0)

# Time Complexity: O(k * 2^n) where n is the number of elements in the input array. In the worst case, we may have to explore all possible combinations of elements to form k subsets.
# Space Complexity: O(n) for the recursion stack and the used array.