# 347. Top K Frequent Elements

# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)
        for num in nums:
            d[num] += 1
        heap = []
        for key, value in d.items():
            if len(heap) < k or value > heap[0][0]:
                heapq.heappush(heap, [value, key])
            if len(heap) > k:
                heapq.heappop(heap)
        return [i[1] for i in heap]