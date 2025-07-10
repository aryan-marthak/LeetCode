# 2300. Successful Pairs of Spells and Potions

# You are given two positive integer arrays spells and potions, of length n and m respectively, where spells[i] represents the strength of the ith spell and potions[j] represents the strength of the jth potion.

# You are also given an integer success. A spell and potion pair is considered successful if the product of their strengths is at least success.

# Return an integer array pairs of length n where pairs[i] is the number of potions that will form a successful pair with the ith spell.

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        # SORTING AND BINARY SEARCH
        
        potions.sort()
        res = []

        for i in spells:
            l, r = 0, len(potions) - 1
            temp = len(potions)

            while l <= r:
                m = l + ((r - l) // 2)
                if i * potions[m] >= success:
                    r = m - 1
                    temp = m
                else:
                    l = m + 1
            res.append(len(potions) - temp)
        return res
    
        # BRUTE FORCE
        
        res = []
        for i in spells:
            count = 0 
            for j in potions:
                if i * j >= success:
                    count += 1
            res.append(count)
        return res