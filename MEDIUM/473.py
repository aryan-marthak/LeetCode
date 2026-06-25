# 473. Matchsticks to Square

# You are given an integer array matchsticks where matchsticks[i] is the length of the ith matchstick. You want to use all the matchsticks to make one square. You should not break any stick, but you can link them up, and each matchstick must be used exactly one time.

# Return true if you can make this square and false otherwise.

class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        side = sum(matchsticks) // 4
        edges = [0] * 4
        matchsticks.sort(reverse = True)
        if sum(matchsticks) / 4 != side:
            return False
        
        def bt(i):
            if i == len(matchsticks):
                return True

            for j in range(4):
                if matchsticks[i] + edges[j] <= side:
                    edges[j] += matchsticks[i]
                    if bt(i + 1):
                        return True
                    edges[j] -= matchsticks[i]
            return False
        return bt(0)
# Time Complexity: O(4^N) where N is the number of matchsticks. In the worst case, we have to try all possible combinations of matchsticks to form the square.
# Space Complexity: O(N) for the recursion stack.