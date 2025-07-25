# 875. Koko Eating Bananas

# Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

# Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

# Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

# Return the minimum integer k such that she can eat all the bananas within h hours.

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # BINARY SEARCH (O(nlogm) -> n = length of piles array, m = maximum of the piles array)
        
        l, r = 1, max(piles)

        while l <= r:
            m = l + (r - l) // 2
            time = 0
            for i in piles:
                time += math.ceil(i / m)

            if time <= h:
                r = m - 1
            else:
                l = m + 1
        return l
        
        # BRUTE FORCE
        
        eat = 1
        
        while True:
            time = 0
            for i in piles:
                time += math.ceil(i / eat)
            
            if time <= h:
                return eat
            eat += 1
        return eat