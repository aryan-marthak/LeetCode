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

# Sorting
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for i in nums:
            count[i] = 1 + count.get(i, 0)

        arr = []
        for i, j in count.items():
            arr.append([j, i])
        arr.sort()

        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res

# Bucket Sort
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            count[num] = 1 + count.get(num, 0)
        for num, cnt in count.items():
            freq[cnt].append(num)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res