# 904. Fruit Into Baskets

# You are visiting a farm that has a single row of fruit trees arranged from left to right. The trees are represented by an integer array fruits where fruits[i] is the type of fruit the ith tree produces.

# You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:

#     You only have two baskets, and each basket can only hold a single type of fruit. There is no limit on the amount of fruit each basket can hold.
#     Starting from any tree of your choice, you must pick exactly one fruit from every tree (including the start tree) while moving to the right. The picked fruits must fit in one of your baskets.
#     Once you reach a tree with fruit that cannot fit in your baskets, you must stop.

# Given the integer array fruits, return the maximum number of fruits you can pick.

# BRUTE FORCE Approach

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        max_len = 0
        for i in range(len(fruits)):
            Set = set()
            for j in range(i, len(fruits)):
                Set.add(fruits[j])
                if len(Set) <= 2:
                    max_len = max(max_len, j - i + 1)
                else:
                    break
        return max_len