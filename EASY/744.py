# 744. Find Smallest Letter Greater Than Target

# You are given an array of characters letters that is sorted in non-decreasing order, and a character target. There are at least two different characters in letters.

# Return the smallest character in letters that is lexicographically greater than target. If such a character does not exist, return the first character in letters.

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        if target >= letters[-1]:
            return letters[0]
        if target < letters[0]:
            return letters[0]
        l, r = 0, len(letters) - 1
        while l < r:
            mid = l + (r - l) // 2

            if target >= letters[mid]:
                l = mid + 1
            else:
                r = mid
        return letters[l]