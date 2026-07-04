# 1405. Longest Happy String

# A string s is called happy if it satisfies the following conditions:

#     s only contains the letters 'a', 'b', and 'c'.
#     s does not contain any of "aaa", "bbb", or "ccc" as a substring.
#     s contains at most a occurrences of the letter 'a'.
#     s contains at most b occurrences of the letter 'b'.
#     s contains at most c occurrences of the letter 'c'.

# Given three integers a, b, and c, return the longest possible happy string. If there are multiple longest happy strings, return any of them. If there is no such string, return the empty string "".

# A substring is a contiguous sequence of characters within a string.

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        res = ""
        maxheap = []
        for i, j in [(-a, "a"), (-b, "b"), (-c, "c")]:
            if i != 0:
                heapq.heappush(maxheap, (i, j))
        while maxheap:
            i, j = heapq.heappop(maxheap)
            if len(res) > 1 and res[-1] == res[-2] ==j:
                if not maxheap:
                    break
                i2, j2 = heapq.heappop(maxheap)
                res += j2
                i2 += 1
                if i2:
                    heapq.heappush(maxheap, (i2, j2))
                heapq.heappush(maxheap, (i, j))
            else:
                res += j
                i += 1
                if i:
                    heapq.heappush(maxheap, (i, j))
        return res
                