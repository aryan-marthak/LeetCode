# 767. Reorganize String

# Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.

# Return any possible rearrangement of s or return "" if not possible.

class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        maxheap = [[-j, i] for i, j in count.items()]
        heapq.heapify(maxheap)

        prev = None
        res = ""

        while maxheap and prev:
            if prev and not maxheap:
                return ""
            
            i, v = heapq.heappop(maxheap)
            res += v
            i += 1

            if prev:
                heapq.heappush(maxheap, prev)
                prev = None
            if cnt != 0:
                prev = [i, v]
        return res