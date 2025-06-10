# 2379. Minimum Recolors to Get K Consecutive Black Blocks

# You are given a 0-indexed string blocks of length n, where blocks[i] is either 'W' or 'B', representing the color of the ith block. The characters 'W' and 'B' denote the colors white and black, respectively.

# You are also given an integer k, which is the desired number of consecutive black blocks.

# In one operation, you can recolor a white block such that it becomes a black block.

# Return the minimum number of operations needed such that there is at least one occurrence of k consecutive black blocks.

class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        l = 0
        recolor = 0
        res = k

        for r in range(len(blocks)):
            if blocks[r] == "W":
                recolor += 1
            if r - l + 1 == k:
                res = min(res, recolor)
                if blocks[l] == "W":
                    recolor -= 1
                l += 1
        return res