# 1011. Capacity To Ship Packages Within D Days

# A conveyor belt has packages that must be shipped from one port to another within days days.

# The ith package on the conveyor belt has a weight of weights[i]. Each day, we load the ship with packages on the conveyor belt (in the order given by weights). We may not load more weight than the maximum weight capacity of the ship.

# Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being shipped within days days.

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # BRUTE FORCE Approach
        
        lbound = max(weights)
        rbound = sum(weights)
        for i in range(lbound, rbound + 1):
            D = 1
            curr_w = 0
            for j in weights:
                if curr_w + j > i:
                    D += 1
                    curr_w = 0
                curr_w += j
            if D <= days:
                return i