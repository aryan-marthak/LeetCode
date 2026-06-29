# 912. Sort an Array

# Given an array of integers nums, sort the array in ascending order and return it.

# You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the smallest space complexity possible.

# Merge Sort
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def mergesort(nums):
            if len(nums) > 1:
                left = nums[:len(nums) // 2]
                right = nums[len(nums) // 2:]

                mergesort(left)
                mergesort(right)

                i, j, k = 0, 0, 0

                while i < len(left) and j < len(right):
                    if left[i] < right[j]:
                        nums[k] = left[i]
                        i += 1
                    else:
                        nums[k] = right[j]
                        j += 1
                    k += 1

                while i < len(left):
                    nums[k] = left[i]
                    i += 1
                    k += 1
                while j < len(right):
                    nums[k] = right[j]
                    j += 1
                    k += 1
        mergesort(nums)
        return nums
# Time Complexity: O(nlog(n))
# Space Complexity: O(n)

# Bubble Sort
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        for i in range(len(nums) - 1, -1, -1):
            for j in range(i):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
        return nums
# Time Complexity: O(n^2)
# Space Complexity: O(1)

# Selection Sort
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            min_idx = i
            for j in range(i + 1, len(nums)):
                if nums[j] < nums[min_idx]:
                    min_idx = j
            nums[i], nums[min_idx] = nums[min_idx], nums[i]
        return nums
# Time Complexity: O(n^2)
# Space Complexity: O(1)

# Insertion Sort
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            key = nums[i]
            j = i
            while j > 0 and key < nums[j - 1]:
                nums[j] = nums[j - 1]
                j -= 1
            nums[j] = key
        return nums
# Time Complexity: O(n^2)
# Space Complexity: O(1)
