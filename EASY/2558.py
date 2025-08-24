# 2558. Take Gifts From the Richest Pile

# You are given an integer array gifts denoting the number of gifts in various piles. Every second, you do the following:

#     Choose the pile with the maximum number of gifts.
#     If there is more than one pile with the maximum number of gifts, choose any.
#     Reduce the number of gifts in the pile to the floor of the square root of the original number of gifts in the pile.

# Return the number of gifts remaining after k seconds.

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        # MAXHEAP
        
        for i in range(len(gifts)):
            gifts[i] = -gifts[i]
        heapq.heapify(gifts)

        for _ in range(k):
            n = -heapq.heappop(gifts)
            heapq.heappush(gifts, -floor(sqrt(n)))

        return -sum(gifts)
        
        # SIMULATION Method
        
        # for i in range(k):
        #     l = 0
        #     for j in range(1, len(gifts)):
        #         if gifts[j] > gifts[l]:
        #             l = j
        #     gifts[l] = int(sqrt(gifts[l])) 
        # return sum(gifts)