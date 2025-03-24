# 2336. Smallest Number in Infinite Set

# You have a set which contains all positive integers [1, 2, 3, 4, 5, ...].

# Implement the SmallestInfiniteSet class:

#     SmallestInfiniteSet() Initializes the SmallestInfiniteSet object to contain all positive integers.
#     int popSmallest() Removes and returns the smallest integer contained in the infinite set.
#     void addBack(int num) Adds a positive integer num back into the infinite set, if it is not already in the infinite set.

class SmallestInfiniteSet:

    def __init__(self):
        self.smallest = 1
        self.removed = set()

    def popSmallest(self) -> int:
        ret = self.smallest
        self.removed.add(ret)
        self.smallest += 1
        while self.smallest in self.removed:
            self.smallest += 1
        return ret       

    def addBack(self, num: int) -> None:
        if num in self.removed:
            self.removed.remove(num)
            if num < self.smallest:
                self.smallest = num 


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)