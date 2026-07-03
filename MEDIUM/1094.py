# 1094. Car Pooling

# There is a car with capacity empty seats. The vehicle only drives east (i.e., it cannot turn around and drive west).

# You are given the integer capacity and an array trips where trips[i] = [numPassengersi, fromi, toi] indicates that the ith trip has numPassengersi passengers and the locations to pick them up and drop them off are fromi and toi respectively. The locations are given as the number of kilometers due east from the car's initial location.

# Return true if it is possible to pick up and drop off all passengers for all the given trips, or false otherwise.

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key = lambda t : t[1])
        minheap = []
        currpass = 0

        for t in trips:
            numpass, start, end = t

            while minheap and minheap[0][0] <= start:
                currpass -= minheap[0][1]
                heapq.heappop(minheap)
            
            currpass += numpass
            if currpass > capacity:
                return False
            heapq.heappush(minheap, [end, numpass])
        return True